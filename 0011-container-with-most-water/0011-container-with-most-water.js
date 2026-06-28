/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let max_area = 0;
    let start = 0;
    let end = height.length - 1

    while(start < end){
        const current_area = Math.min(height[start], height[end]) * (end - start) // height * width

        if (height[start] <= height[end]){
            start += 1
        } else {
            end -= 1
        }
        max_area = Math.max(max_area, current_area)
    }
    return max_area;
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna