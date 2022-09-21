"""Tests for neurodsp.plts.style."""

import matplotlib.pyplot as plt

from neurodsp.plts.settings import TITLE_FONTSIZE

from neurodsp.tests.tutils import plot_test

from neurodsp.plts.style import *

###################################################################################################
###################################################################################################

def test_check_style_options():

    check_style_options()

def test_apply_axis_style():

    _, ax = plt.subplots()

    title = 'Ploty McPlotface'
    xlim = (1.0, 10.0)
    ylabel = 'Line Value'

    apply_axis_style(ax, title=title, xlim=xlim, ylabel=ylabel)

    assert ax.get_title() == title
    assert ax.get_xlim() == xlim
    assert ax.get_ylabel() == ylabel

def test_apply_line_style():

    # Check applying style to one line
    _, ax = plt.subplots()
    ax.plot([1, 2], [3, 4])

    lw = 4
    apply_line_style(ax, lw=lw)

    assert ax.get_lines()[0].get_lw() == lw

    # Check applying style to multiple lines
    _, ax = plt.subplots()
    ax.plot([1, 2], [[3, 4], [5, 6]])

    alphas = [0.5, 0.75]
    apply_line_style(ax, alpha=alphas)

    for line, alpha in zip(ax.get_lines(), alphas):
        assert line.get_alpha() == alpha

def test_apply_custom_style():

    _, ax = plt.subplots()
    ax.set_title('placeholder')

    # Test simple application of custom plot style
    apply_custom_style(ax)
    assert ax.title.get_size() == TITLE_FONTSIZE

    # Test adding input parameters to custom plot style
    new_title_fontsize = 15.0
    apply_custom_style(ax, title_fontsize=new_title_fontsize)
    assert ax.title.get_size() == new_title_fontsize

def test_plot_style():

    _, ax = plt.subplots()

    def my_custom_styler(ax, **kwargs):
        ax.set_title('DATA!')

    # Apply plot style using defaults
    plot_style(ax)

    # Apply plot style passing in a styler
    plot_style(ax, custom_styler=my_custom_styler)

@plot_test
def test_style_plot():

    @style_plot
    def example_plot():
        plt.plot([1, 2], [3, 4])

    def my_plot_style(ax, **kwargs):
        ax.set_title('Custom!')

    # Test with applying default custom styling
    lw = 5
    title = 'Science.'
    example_plot(title=title, lw=lw)

    # Test with passing in own plot_style function
    example_plot(plot_style=my_plot_style)
