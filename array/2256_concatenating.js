/**
 * @param {number[]} nums
 * @return {number}
 */
var findTheArrayConcVal = function(nums) {
    if (nums.length == 1) return nums[0];

    let n = nums.length - 1;
    let newArr = [];

    for (let i = 0; i < Math.floor(nums.length / 2); i++) {
        newArr.push(Number([nums[i].toString() + nums[n - i].toString()]));
    }

    return newArr.reduce((x, c) => x + c, 0);
};

let result  = findTheArrayConcVal([5,14,13,8,12]);
console.log(result);