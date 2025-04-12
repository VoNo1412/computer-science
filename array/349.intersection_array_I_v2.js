/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
   let setNums1 = new Set(nums1);
   let setNums2 = new Set(nums2);

   return [...setNums1].filter(x => [...setNums2].has(x));
};

// let result = intersection([1,2,2,1], [2, 2]);
let result = intersection([4,9,5], [9,4,9,8,4]);
console.log(result);