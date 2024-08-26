#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
A peak is defined as an element that is greater than or equal to its neighbors.
"""

def find_peak(list_of_integers):
    """
    Function to find a peak element in a list of integers.
    :param list_of_integers: List of unsorted integers.
    :return: A peak element or None if the list is empty.
    """
    if not list_of_integers:
        return None

    def binary_search_peak(start, end):
        """
        Helper function to perform binary search to find a peak.
        :param start: Start index of the current search range.
        :param end: End index of the current search range.
        :return: A peak element.
        """
        mid = (start + end) // 2
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        # If the left neighbor is greater, search in the left half
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search_peak(start, mid - 1)
        # If the right neighbor is greater, search in the right half
        else:
            return binary_search_peak(mid + 1, end)

    return binary_search_peak(0, len(list_of_integers) - 1)

