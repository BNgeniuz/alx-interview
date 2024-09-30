#!/usr/bin/python3
"""
Main file for testing
"""

def makeChange(coins, total):
    """
    How many of this type of coin can I get with my money? Okay,
        I'll take that many. Now, how much money do I have left?
        And how many coins do I have in my pocket?
    """
    if total <= 0:
        return 0
    elif total > 0:
        newList = sorted(coins[:])
        newList = list(reversed(newList))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(newList)):
            if value >= newList[index]:
                value = value - newList[index]
                count += 1
            elif value < newList[index]:
                index += 1
        if index == len(newList):
            if value != 0:
                return -1
            elif value == 0:
                return count
