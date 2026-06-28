/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    let n = s.length;
    let max = 0;
    let ans = "";
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            if (chack_palindrom(s, i, j) && max < j - i + 1) {
                max = j - i + 1;
                ans = s.substring(i, j + 1);
            }
        }
    }
    return ans;
};

function chack_palindrom(str, i, j) {
    while (i < j) {
        if (str[i] != str[j]) {
            return false;
        }
        i++;
        j--;
    }

    return true
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna