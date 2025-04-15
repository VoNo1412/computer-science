/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let total = 0;
    nums.forEach(x => {
        let nu = x.toString().split("").length;
        if (nu % 2 == 0) {
            total += 1;
        }
    })
    console.log(total)
    return total;
};

let nums = [12,345,2,6,7896];
findNumbers(nums);