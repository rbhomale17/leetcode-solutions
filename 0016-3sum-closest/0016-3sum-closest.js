/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b)

    nearest = nums[0] + nums[1] + nums[2]
    for(let i = 0; i<nums.length; i++){
        if (i > 0 && nums[i] == nums[i - 1]) {continue}

        let start = i + 1
        let end = nums.length - 1

        while (start < end){
            total = nums[i] + nums[start] + nums[end]

            if (Math.abs(target - total) < Math.abs(target - nearest)){
                nearest = total
            }
            if (total === target){
                return total
            } else if (total < target){
                start += 1
            } else {
                end -= 1
            }
        }
    }
    return nearest
};

