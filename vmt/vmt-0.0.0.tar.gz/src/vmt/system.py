#!/usr/bin/env python3
import subprocess


class OpenerError(Exception):
    '''Exception raised when command fails'''

    def __init__(self, error, message='ERROR: Failed to run'):
        self.error = error
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} {self.error}'


def browse_base(user):
    '''
    Browse a user's base directory with their desired program
    '''

    base_dir = user.base_dir

    try:
        opener = user.file_manager
        opener.append(base_dir)

    except KeyError:
        msg = 'ERROR: file_manager is not set in'
        raise OpenerError(user.conf_file, message=msg)

    try:
        open_process(opener)

    except OpenerError as err:
        print(err)
        return 1


def open_process(opener):
    '''Open a program with the given opener list'''

    try:
        subprocess.Popen(opener,
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.STDOUT)

    except (subprocess.CalledProcessError, FileNotFoundError):
        raise OpenerError(opener)
