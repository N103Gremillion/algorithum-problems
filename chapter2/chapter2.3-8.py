from xmlrpc.client import boolean


def mergeSort(nums: list[int], l: int, r: int) -> list[int]:
  if not nums or l > r:
    return []
  if l == r:
    return [nums[l]]

  m: int = (l+r) // 2
  leftNums: list[int] = mergeSort(nums, l, m)
  rightNums: list[int] = mergeSort(nums, m+1, r)
  return merge(leftNums, rightNums)

def merge(nums1: list[int], nums2: list[int]) -> list[int]:
  # nums1
  i: int = 0
  n: int = len(nums1)

  # nums2
  j: int = 0
  m: int = len(nums2)

  res: list[int] = []

  while (i < n and j < m):
    if (nums1[i] <= nums2[j]):
      res.append(nums1[i])
      i += 1
    else:
      res.append(nums2[j])
      j += 1
  
  if i >= n:
    res.extend(nums2[j:m])
  else:
    res.extend(nums1[i:n])
  
  return res

# assumes a sorted array (if num at i then doesn't count cuz that is the other num's index)
def binarySearch(nums: list[int], i: int, x: int) -> bool:
  l: int = 0
  r: int = len(nums)-1

  while(l < r):
    m: int = (l+r)//2
    num: int = nums[m]

    if (num == x and i != m):
      return True
    elif (num == x and i == m):
      left = nums[i-1] if i > 0 else None
      right = nums[i+1] if i < r else None
      if left == num or right == num:
        return True
      else:
        return False
    elif (num > x):
      r = m
    else:
      l = m+1

  return False

# function that determines if nums contains 2 elements that sum to x
def containsTwoElementsSum(nums: list[int], x: int) -> boolean:
  n: int = len(nums)

  if n < 2:
    return False

  sortedNums: list[int] = mergeSort(nums, 0, len(nums)-1)
  for i in range(len(nums)):
    num: int = nums[i]
    if (binarySearch(nums, i, x-num)):
      return True
    
  return False

array: list[int] = [100, 43, 54, 23, 67, 1, 9, 413, 456, 21, 46, 80, 70]
sortedArray: list[int] = mergeSort(array, 0, len(array)-1)

print(array)
print(sortedArray)
print(containsTwoElementsSum(sortedArray, 18))