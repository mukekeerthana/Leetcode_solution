#include <limits.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure nums1 is the smaller array
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }

    int m = nums1Size;
    int n = nums2Size;
    int low = 0, high = m;

    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = (m + n + 1) / 2 - partitionX;

        int maxLeftX = (partitionX == 0)? INT_MIN : nums1[partitionX - 1];
        int minRightX = (partitionX == m)? INT_MAX : nums1[partitionX];

        int maxLeftY = (partitionY == 0)? INT_MIN : nums2[partitionY - 1];
        int minRightY = (partitionY == n)? INT_MAX : nums2[partitionY];

        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            // Found correct partition
            if ((m + n) % 2 == 0) {
                int leftMax = maxLeftX > maxLeftY? maxLeftX : maxLeftY;
                int rightMin = minRightX < minRightY? minRightX : minRightY;
                return (leftMax + rightMin) / 2.0;
            } else {
                return maxLeftX > maxLeftY? maxLeftX : maxLeftY;
            }
        } else if (maxLeftX > minRightY) {
            high = partitionX - 1; // move left in nums1
        } else {
            low = partitionX + 1; // move right in nums1
        }
    }

    return 0.0; // should not reach here
}