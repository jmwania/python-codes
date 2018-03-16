# https://www.codewars.com/kata/merge-two-sorted-arrays-into-one/train/python
def merge_arrays(arr1, arr2):
  return sorted(list(set(arr1+arr2)))