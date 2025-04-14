/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = {};
    let result = null
    nums.map((x, i) => {
        let subNum = target - x;
        if (map[subNum] >= 0) {
            result = [map[subNum], i]
        }
        map[x] = i
    })

    let newD = new Set([1, 2, 3]);
    console.log(newD)
    return result
};

const result = twoSum([2,7,11,15], 9);
// const result = twoSum([3,2,4], 6);
// const result = twoSum([3,3], 6);
console.log(result);