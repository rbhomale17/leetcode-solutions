/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {

 if (!strs.length) return '';

    // Sort the array of strings to ensure the shortest string is first
    strs.sort();

    // Take the first string as the reference for comparison
    let prefix = strs[0];

    // Iterate through the characters of the reference string
    for (let i = 0; i < prefix.length; i++) {
        // Compare each character with the corresponding character in other strings
        for (let j = 1; j < strs.length; j++) {
            if (prefix[i] !== strs[j][i]) {
                return prefix.substring(0, i); // Return the prefix up to the current character if there's a mismatch
            }
        }
    }
    return prefix; // Return the full prefix if all strings match up to the length of the shortest string
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna