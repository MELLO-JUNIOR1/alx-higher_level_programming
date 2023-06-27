#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        new = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        '''
        print("Exception: {}".format(e), file=sys.stderr)
        '''
        return None
    return new
