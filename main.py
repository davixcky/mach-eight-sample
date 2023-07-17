# -*- coding: utf-8 -*-
"""Mach Eight Sample Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G3gAWJGZm-0_SDoZ0p5_CcRXYqBIBttn

## Mach Eight Sample Project
*David Orozco*


## Problem Thinking
We know that sum is basically `a + b = c`, so we have to calculate and get two nums from the list that sums `c`. The way to access to each of these numbers is by iterating over the list. Once we access over each value, we could say we have `a` (and `c` which is the target), so we can substract and know what is the missing number, `b = c - a`. By doing this we can know easily what is the missing number to complete the pair. If we never found the missing number, means it didn't have a pair.
"""

import sys

def get_list_of_pairs_eq_target(integers_lst = [], target = 0):
  accepted_sums = []
  remains = {}
  for val in integers_lst:
    if val in remains:
      accepted_sums.append([remains[val], val])
      del remains[val]
    else:
      remains[target - val] = val
  return accepted_sums

def print_pretty(list_of_pairs):
  for idx, pair in enumerate(list_of_pairs):
    print('{}. {} + {} = {}'.format(idx, pair[0], pair[1], sum(pair)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <list_of_integers> <target>")
        sys.exit(1)

    list_of_integers = sys.argv[1]
    target = int(sys.argv[2])

    parsed_list = [int(num) for num in list_of_integers.split(',')]
    result = get_list_of_pairs_eq_target(parsed_list, target)
    print("Result:", result)
    print_pretty(result)


"""The results will appear based of the firsts sums pairs found and not on the first elements inserted on the possible dictionary"""