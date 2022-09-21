#  Copyright 2008-2015 Nokia Networks
#  Copyright 2016-     Robot Framework Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Interface to ease traversing through a test suite structure.

Visitors make it easy to modify test suite structures or to collect information
from them. They work both with the :mod:`executable model <robot.running.model>`
and the :mod:`result model <robot.result.model>`, but the objects passed to
the visitor methods are slightly different depending on the model they are
used with. The main differences are that on the execution side keywords do
not have child keywords nor messages, and that only the result objects have
status related attributes like :attr:`status` and :attr:`starttime`.

This module contains :class:`SuiteVisitor` that implements the core logic to
visit a test suite structure, and the :mod:`~robot.result` package contains
:class:`~robot.result.visitor.ResultVisitor` that supports visiting the whole
test execution result structure. Both of these visitors should be imported
via the :mod:`robot.api` package when used by external code.

Visitor algorithm
-----------------

All suite, test, keyword and message objects have a :meth:`visit` method that
accepts a visitor instance. These methods will then call the correct visitor
method :meth:`~SuiteVisitor.visit_suite`, :meth:`~SuiteVisitor.visit_test`,
:meth:`~SuiteVisitor.visit_keyword` or :meth:`~SuiteVisitor.visit_message`,
depending on the instance where the :meth:`visit` method exists.

The recommended and definitely the easiest way to implement a visitor is extending
the :class:`SuiteVisitor` base class. The default implementation of its
:meth:`visit_x` methods take care of traversing child elements of the object
:obj:`x` recursively. A :meth:`visit_x` method first calls a corresponding
:meth:`start_x` method (e.g. :meth:`visit_suite` calls :meth:`start_suite`),
then calls :meth:`visit` for all child objects of the :obj:`x` object, and
finally calls the corresponding :meth:`end_x` method. The default
implementations of :meth:`start_x` and :meth:`end_x` do nothing.

All items that can appear inside tests have their own visit methods. These
include :meth:`visit_keyword`, :meth:`visit_message` (only applicable with
results, not with executable data), :meth:`visit_for`, :meth:`visit_if`, and
so on, as well as their appropriate ``start/end`` methods like :meth:`start_keyword`
and :meth:`end_for`. If there is a need to visit all these items, it is possible to
implement only :meth:`start_body_item` and :meth:`end_body_item` methods that are,
by default, called by the appropriate ``start/end`` methods. These generic methods
are new in Robot Framework 5.0.

Visitors extending the :class:`SuiteVisitor` can stop visiting at a certain
level either by overriding suitable :meth:`visit_x` method or by returning
an explicit ``False`` from any :meth:`start_x` method.

Examples
--------

The following example visitor modifies the test suite structure it visits.
It could be used, for example, with Robot Framework's ``--prerunmodifier``
option to modify test data before execution.

.. literalinclude:: ../../../doc/api/code_examples/SelectEveryXthTest.py
   :language: python

For more examples it is possible to look at the source code of visitors used
internally by Robot Framework itself. Some good examples are
:class:`~robot.model.tagsetter.TagSetter` and
:mod:`keyword removers <robot.result.keywordremover>`.
"""


class SuiteVisitor:
    """Abstract class to ease traversing through the suite structure.

    See the :mod:`module level <robot.model.visitor>` documentation for more
    information and an example.
    """

    def visit_suite(self, suite):
        """Implements traversing through suites.

        Can be overridden to allow modifying the passed in ``suite`` without
        calling :meth:`start_suite` or :meth:`end_suite` nor visiting child
        suites, tests or setup and teardown at all.
        """
        if self.start_suite(suite) is not False:
            if suite.has_setup:
                suite.setup.visit(self)
            suite.suites.visit(self)
            suite.tests.visit(self)
            if suite.has_teardown:
                suite.teardown.visit(self)
            self.end_suite(suite)

    def start_suite(self, suite):
        """Called when a suite starts. Default implementation does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        pass

    def end_suite(self, suite):
        """Called when a suite ends. Default implementation does nothing."""
        pass

    def visit_test(self, test):
        """Implements traversing through tests.

        Can be overridden to allow modifying the passed in ``test`` without calling
        :meth:`start_test` or :meth:`end_test` nor visiting the body of the test.
        """
        if self.start_test(test) is not False:
            if test.has_setup:
                test.setup.visit(self)
            test.body.visit(self)
            if test.has_teardown:
                test.teardown.visit(self)
            self.end_test(test)

    def start_test(self, test):
        """Called when a test starts. Default implementation does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        pass

    def end_test(self, test):
        """Called when a test ends. Default implementation does nothing."""
        pass

    def visit_keyword(self, kw):
        """Implements traversing through keywords.

        Can be overridden to allow modifying the passed in ``kw`` without
        calling :meth:`start_keyword` or :meth:`end_keyword` nor visiting
        the body of the keyword
        """
        if self.start_keyword(kw) is not False:
            if hasattr(kw, 'body'):
                kw.body.visit(self)
            if kw.has_teardown:
                kw.teardown.visit(self)
            self.end_keyword(kw)

    def start_keyword(self, keyword):
        """Called when a keyword starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(keyword)

    def end_keyword(self, keyword):
        """Called when a keyword ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(keyword)

    def visit_for(self, for_):
        """Implements traversing through FOR loops.

        Can be overridden to allow modifying the passed in ``for_`` without
        calling :meth:`start_for` or :meth:`end_for` nor visiting body.
        """
        if self.start_for(for_) is not False:
            for_.body.visit(self)
            self.end_for(for_)

    def start_for(self, for_):
        """Called when a FOR loop starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(for_)

    def end_for(self, for_):
        """Called when a FOR loop ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(for_)

    def visit_for_iteration(self, iteration):
        """Implements traversing through single FOR loop iteration.

        This is only used with the result side model because on the running side
        there are no iterations.

        Can be overridden to allow modifying the passed in ``iteration`` without
        calling :meth:`start_for_iteration` or :meth:`end_for_iteration` nor visiting
        body.
        """
        if self.start_for_iteration(iteration) is not False:
            iteration.body.visit(self)
            self.end_for_iteration(iteration)

    def start_for_iteration(self, iteration):
        """Called when a FOR loop iteration starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(iteration)

    def end_for_iteration(self, iteration):
        """Called when a FOR loop iteration ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(iteration)

    def visit_if(self, if_):
        """Implements traversing through IF/ELSE structures.

        Notice that ``if_`` does not have any data directly. Actual IF/ELSE branches
        are in its ``body`` and visited using :meth:`visit_if_branch`.

        Can be overridden to allow modifying the passed in ``if_`` without
        calling :meth:`start_if` or :meth:`end_if` nor visiting branches.
        """
        if self.start_if(if_) is not False:
            if_.body.visit(self)
            self.end_if(if_)

    def start_if(self, if_):
        """Called when an IF/ELSE structure starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(if_)

    def end_if(self, if_):
        """Called when an IF/ELSE structure ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(if_)

    def visit_if_branch(self, branch):
        """Implements traversing through single IF/ELSE branch.

        Can be overridden to allow modifying the passed in ``branch`` without
        calling :meth:`start_if_branch` or :meth:`end_if_branch` nor visiting body.
        """
        if self.start_if_branch(branch) is not False:
            branch.body.visit(self)
            self.end_if_branch(branch)

    def start_if_branch(self, branch):
        """Called when an IF/ELSE branch starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(branch)

    def end_if_branch(self, branch):
        """Called when an IF/ELSE branch ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(branch)

    def visit_try(self, try_):
        """Implements traversing through TRY/EXCEPT structures.

        This method is used with the TRY/EXCEPT root element. Actual TRY, EXCEPT, ELSE
        and FINALLY branches are visited separately using :meth:`visit_try_branch`.
        """
        if self.start_try(try_) is not False:
            try_.body.visit(self)
            self.end_try(try_)

    def start_try(self, try_):
        """Called when a TRY/EXCEPT structure starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(try_)

    def end_try(self, try_):
        """Called when a TRY/EXCEPT structure ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(try_)

    def visit_try_branch(self, branch):
        """Visits individual TRY, EXCEPT, ELSE and FINALLY branches."""
        if self.start_try_branch(branch) is not False:
            branch.body.visit(self)
            self.end_try_branch(branch)

    def start_try_branch(self, branch):
        """Called when TRY, EXCEPT, ELSE or FINALLY branches start.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(branch)

    def end_try_branch(self, branch):
        """Called when TRY, EXCEPT, ELSE and FINALLY branches end.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(branch)

    def visit_while(self, while_):
        """Implements traversing through WHILE loops.

        Can be overridden to allow modifying the passed in ``while_`` without
        calling :meth:`start_while` or :meth:`end_while` nor visiting body.
        """
        if self.start_while(while_) is not False:
            while_.body.visit(self)
            self.end_while(while_)

    def start_while(self, while_):
        """Called when a WHILE loop starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(while_)

    def end_while(self, while_):
        """Called when a WHILE loop ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(while_)

    def visit_while_iteration(self, iteration):
        """Implements traversing through single WHILE loop iteration.

        This is only used with the result side model because on the running side
        there are no iterations.

        Can be overridden to allow modifying the passed in ``iteration`` without
        calling :meth:`start_while_iteration` or :meth:`end_while_iteration` nor visiting
        body.
        """
        if self.start_while_iteration(iteration) is not False:
            iteration.body.visit(self)
            self.end_while_iteration(iteration)

    def start_while_iteration(self, iteration):
        """Called when a WHILE loop iteration starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(iteration)

    def end_while_iteration(self, iteration):
        """Called when a WHILE loop iteration ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(iteration)

    def visit_return(self, return_):
        """Visits a RETURN elements."""
        if self.start_return(return_) is not False:
            if hasattr(return_, 'body'):
                return_.body.visit(self)
            self.end_return(return_)

    def start_return(self, return_):
        """Called when a RETURN element starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(return_)

    def end_return(self, return_):
        """Called when a RETURN element ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(return_)

    def visit_continue(self, continue_):
        """Visits CONTINUE elements."""
        if self.start_continue(continue_) is not False:
            if hasattr(continue_, 'body'):
                continue_.body.visit(self)
            self.end_continue(continue_)

    def start_continue(self, continue_):
        """Called when a CONTINUE element starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(continue_)

    def end_continue(self, continue_):
        """Called when a CONTINUE element ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(continue_)

    def visit_break(self, break_):
        """Visits BREAK elements."""
        if self.start_break(break_) is not False:
            if hasattr(break_, 'body'):
                break_.body.visit(self)
            self.end_break(break_)

    def start_break(self, break_):
        """Called when a BREAK element starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(break_)

    def end_break(self, break_):
        """Called when a BREAK element ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(break_)

    def visit_message(self, msg):
        """Implements visiting messages.

        Can be overridden to allow modifying the passed in ``msg`` without
        calling :meth:`start_message` or :meth:`end_message`.
        """
        if self.start_message(msg) is not False:
            self.end_message(msg)

    def start_message(self, msg):
        """Called when a message starts.

        By default, calls :meth:`start_body_item` which, by default, does nothing.

        Can return explicit ``False`` to stop visiting.
        """
        return self.start_body_item(msg)

    def end_message(self, msg):
        """Called when a message ends.

        By default, calls :meth:`end_body_item` which, by default, does nothing.
        """
        self.end_body_item(msg)

    def start_body_item(self, item):
        """Called, by default, when keywords, messages or control structures start.

        More specific :meth:`start_keyword`, :meth:`start_message`, `:meth:`start_for`,
        etc. can be implemented to visit only keywords, messages or specific control
        structures.

        Can return explicit ``False`` to stop visiting. Default implementation does
        nothing.
        """
        pass

    def end_body_item(self, item):
        """Called, by default, when keywords, messages or control structures end.

        More specific :meth:`end_keyword`, :meth:`end_message`, `:meth:`end_for`,
        etc. can be implemented to visit only keywords, messages or specific control
        structures.

        Default implementation does nothing.
        """
        pass
