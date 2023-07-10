#!/usr/bin/python3
"""inherit from the int"""


class MyInt(int):
    """handling the opposit"""
    def __eq__(self, value):
        """usinf the opposit magic class insede the other one"""
        return super().__ne__(value)

    def __ne__(self, value):
        """usinf the opposit magic class insede the other one"""
        return super().__eq__(value)
