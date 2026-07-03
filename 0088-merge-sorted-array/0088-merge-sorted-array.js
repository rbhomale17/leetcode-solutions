/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
    let i = m - 1, j = n - 1;
    let mergedIndex = m + n - 1;

    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[mergedIndex] = nums1[i];
            i--;
        } else {
            nums1[mergedIndex] = nums2[j];
            j--;
        }
        mergedIndex--;
    }

    while (i >= 0) {
        nums1[mergedIndex] = nums1[i];
        i--;
        mergedIndex--;
    }

    while (j >= 0) {
        nums1[mergedIndex] = nums2[j];
        j--;
        mergedIndex--;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna