from xmlrpc.client import boolean

def insertionSort(nums: list[int]) -> list[int]:
  n: int = len(nums)

  res: list[int] = []
  
  for num in nums:
    res.append(num)

  if n == 0:
    return []
  if n == 1:
    return [nums[0]]
  
  i: int = 1

  while (i < n):
    j: int = i-1
    while (res[j] > res[j+1] and j >= 0):
      temp: int = res[j+1]
      res[j+1] = res[j]
      res[j] = temp
      j = j-1
    i += 1
  
  return res

def mergeSort(nums: list[int], l: int, r: int, k: int) -> list[int]:

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
  
  if not nums or l > r:
    return []
  if l == r:
    return [nums[l]]
  if len(nums) <= k:
    return insertionSort(nums)
  
  m: int = (l+r) // 2
  leftNums: list[int] = mergeSort(nums, l, m, k)
  rightNums: list[int] = mergeSort(nums, m+1, r, k)
  return merge(leftNums, rightNums)

array: list[int] = [100, 43, 54, 23, 67, 1, 9, 413, 456, 21, 46, 80, 70]
sortedArray: list[int] = mergeSort(array, 0, len(array)-1, 3)

print(array)
print(sortedArray)
