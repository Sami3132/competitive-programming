/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let count = Array(101).fill(0);

    for (let i = 0; i < nums.length; i++) {
        count[nums[i]]++;
    }

    for (let i = 1; i < count.length; i++) {
        count[i] += count[i - 1];
    }

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 0) nums[i] = 0;
        else nums[i] = count[nums[i] - 1];
    }

    return nums;
};
