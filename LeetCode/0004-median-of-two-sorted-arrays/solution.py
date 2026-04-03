from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            nums1_left = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # Check if partition is valid
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
                else:
                    return float(max(nums1_left, nums2_left))
            elif nums1_left > nums2_right:
                high = i - 1
            else:
                low = i + 1

