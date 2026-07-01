/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let j = 0;
    for(let num of nums){
        if (num != val){
            nums[j++] = num
        }
    }
    console.log(j, nums, nums.slice(0, j))
    return j
};

