/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let result = [];

    for (let num of nums1) {
        let idx = nums2.indexOf(num);
        if(idx != -1) {
            result.push(num);
            nums2.splice(idx, 1);
        }
    }
    return result;
}
// [1, 2, 2, 1] [2] => [2]

console.log(intersect([1, 2, 2, 1], [2, 2]));
