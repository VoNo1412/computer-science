/**
 * @param {number[]} nums
 * @return {number}
 */
var differenceOfSum = function(nums) {
    // the element;
    let totalEl = nums.reduce((x, z) => x + z, 0);
    let totalDigit = 0;
    for (let num of nums) {
        let nu = num.toString().split("");
        if (nu.length > 1) {
            totalDigit += nu.reduce((x, y) => Number(x) + Number(y), 0);    
            continue;
        }
        totalDigit += num
    }

    return Math.abs(totalEl - totalDigit);
};

let result = differenceOfSum([1,2,3,4]);
console.log(result);