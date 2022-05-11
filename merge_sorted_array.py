'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Run loop till we check all the numbers in nums1 and nums2
        while m > 0 and n > 0:
            # Check if the [m]th number of nums1 is greater than the [n]th number of nums2 
            if nums1[m-1] >= nums2[n-1]:
                # Change the [0] value of num1 to the [m]th number of nums1
                nums1[m+n-1] = nums1[m-1]
                # Decrement the value of m, so that next iteration we check the number to the right of m
                m -= 1
            else:
                # Change the [0] value of num1 to the [n]th number of nums2
                nums1[m+n-1] = nums2[n-1]
                # Decrement the value of m, so that next iteration we check the number to the right of n
                n -= 1
        # nums1 = [5,6,7,0,0,0] , m = 3, nums2 = [1,2,3] , n = 3
        # After the while loop, [5,6,7,5,6,7]
        # This if condition will change it to [2, 3, 4, 5, 6, 7]
        if n > 0:
        # This will set the first n elements of nums1 to the n elements of nums2 if num1 has larger integers than num2
            nums1[:n] = nums2[:n]
        return nums1

print(Solution().merge([5,6,7,0,0,0], 3,[2,3,4], 3))

# Time Complexity: O(m + n) , where m and n are the given lengths of the sorted arrays, 
# Since in the worst case the algorithm would need to swap every element of both arrays once (for this case as an example: [4, 5, 6, 0, 0, 0], [1, 2, 3])
# Space Complexity: O(1) space complexity, since no extra memory is necessary