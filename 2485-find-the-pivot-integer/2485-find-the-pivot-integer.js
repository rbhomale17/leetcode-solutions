/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    let pivot = Math.sqrt(n * (n + 1) / 2);
    if(Number.isInteger(pivot)){
        return Math.floor(pivot);
    }else{
        return -1;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna