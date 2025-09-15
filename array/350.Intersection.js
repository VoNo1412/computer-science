/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const hashMap = new Map();

    nums1.forEach(x => {
        if (!hashMap.get(x)) {
            hashMap.set(x, 1)
        }
    });

    let result = [];
    nums2.forEach(x => {
        if (hashMap.get(x)) {
            hashMap.set(x, hashMap.get(x) - 1);
            result.push(x)
        }
    })

    return result
};

// let result = intersection([1,2,2,1], [2, 2]);
let result = intersection([4,9,5], [9,4,9,8,4]);
console.log(result);