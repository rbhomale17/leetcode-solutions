/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    // console.log(heights)
    let arr = heights;
    let n = heights.length
    let st = [];
    let left = [];
    left[0] = -1;
    st.push(0);
    for(let i=1; i<n; i++)
    {
        while(st.length!==0 && heights[st[st.length-1]] >= heights[i])
        {
            st.pop();
        }
        st.length!==0 ? left.push(st[st.length-1]) : left.push(-1);
        st.push(i)
        // console.log(st)
    }
    // console.log(left)

    st = [];
    let right = [];
    right[right.length] = n;
    st.push(n-1);
    // console.log(right)
    for(let i=n-2; i>=0; i--)
    {
        while(st.length!==0 && heights[st[st.length-1]] >= heights[i])
        {
            st.pop();
        }
        st.length!==0 ? right.unshift(st[st.length-1]) : right.unshift(n);
        st.push(i)
        // console.log(st)
    }
    // console.log(right)

    let maxArea = -1;
    for(let i=0; i<n; i++)
    {
        let length = right[i] - left[i] - 1;
        let area = length * arr[i];
        if(maxArea < area)
        {
            maxArea = area;
        }
    }
    return maxArea;
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna