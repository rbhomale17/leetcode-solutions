/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const last_seen_index = {}

    let window_start = 0;

    let max_length = 0;

    for(let window_end = 0; window_end<s.length; window_end++){
        if ( s[window_end] in last_seen_index && last_seen_index[s[window_end]] >= window_start){
            window_start = last_seen_index[s[window_end]] + 1
        }

        last_seen_index[s[window_end]] = window_end

        max_length = Math.max(max_length, window_end - window_start + 1)
    }
    return max_length
};

