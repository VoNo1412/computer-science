/* 
  Array 
*/

// Input: arr = [1,0,2,3,0,4,5,0]
// Output: [1,0,0,2,3,0,0,4]
// Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

// Step 1: if 0 exist array => duplicate 0
// Step 2: shifting remain element => to the right

function duplicateZero(arr) {
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] === 0) {
      for (let j = arr.length - 1; j > i; j--) {
        arr[j] = arr[j - 1];
      }
    }
  }
}


/**
 * 
  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  Output: [1,2,2,3,5,6]
  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
*/

var merge = function (nums1, m, nums2, n) {
  for (let i = 0; i < n + m; i++) {
    if (nums2[i]) {
      nums1[i + m] = nums2[i];
    }


  }


  if (m > 0 && n > 0) {
    for (let i = 0; i < m + n; i++) {
      let temp;
      for (let j = 0; j < m + n; j++) {
        if (nums1[j] > nums1[i]) {
          temp = nums1[i];
          nums1[i] = nums1[j];
          nums1[j] = temp;
        }
      }
    }
  }
};
// merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3);
// merge([0], 0, [1], 1);
// merge([4, 0, 0, 0, 0, 0],
//   1,
//   [1, 2, 3, 5, 6],
//   5);


/** 
 * 
 * Delete
 */

// step 1: remove element
// step 2: shifting left elements
// step 3: count value exist in array
var removeDuplicateElement = function (nums) {
  let hashMap = new Set();
  let left = 0;
  for (let i = 0; i < nums.length; i++) {
    if (hashMap.has(nums[i])) continue;
    nums[left++] = nums[i];
    hashMap.add(nums[i]);
  }


  nums.length = left;
  return hashMap.size;
};

// removeDuplicateElement([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);
// removeDuplicateElement([1, 1, 2]);
// removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2); // expected output: [0, 1, 4, 0, 3]
// removeElement([0, 1, 2, 3], 2);


/**
 * @param Search
 */


var checkIfExist = function (arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] == arr[j] * 2 || arr[j] == arr[i] * 2) {
        return true;
      }
    }
  }

  return false;
};


// console.log(checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
var validMountainArray = function (arr) {
  let isCheck = false;
  if (arr.length < 3) return false;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      isCheck = true;
    } else if (arr[i] === arr[i - 1] || isCheck) {
      return isCheck = false;
    }
  }

  return isCheck;
};

// console.log(validMountainArray([0, 3, 2, 1]))
// console.log(validMountainArray([2, 0, 2]))
// console.log(validMountainArray([0,1,2,1,2]))


/**
 * 
* @abstract in-place is override input Array and not created new array
 */


// step 1: find max element
// step 2: assign value element = max element with i < index max 
// step 3: find max element with condition current i !== index max
// for loop 3 step

function replaceElements(arr) {
  let maxR = -1;
  for (let i = arr.length - 1; i >= 0; i--) {
    let curr = arr[i];
    arr[i] = maxR;
    maxR = Math.max(maxR, curr);
  }

  return arr;
}

// console.log(replaceElements([17, 18, 5, 4, 6, 1]))





/**
 * 
 * Repeat
 */

function removeStoredDupicate(nums) {
  let index = 0, point;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== point) {
      nums[index] = nums[i];
      index++;
    }

    point = nums[i];
  }

  nums.length = index;
  return nums;
}

// console.log(removeStoredDupicate([1, 1, 2]));
// console.log(removeStoredDupicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));



function moveZeros(nums) {
  let index = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      nums[index++] = nums[i];
    }

    if (i >= index) {
      nums[i] = 0;
    }
  }

  return nums;
}

// console.log(moveZeros([0, 1, 2, 0, 3, 12]));
// console.log(moveZeros([1]));
// console.log(moveZeros([0, 1]));


function sortArrayByParity(nums) {
  let odd = [], even = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] % 2 === 0) {
      even.push(nums[i]);
    } else {
      odd.push(nums[i])
    }
  }

  return even.concat(odd);
}


// console.log(sortArrayByParity([3, 1, 2, 4]))
// console.log(sortArrayByParity([0, 1, 2]))


function heightChecker(heights) {
  let initHeights = [...heights];
  let count = 0;
  for (let i = 0; i < heights.length; i++) {
    for (let j = i; j < heights.length; j++) {
      if (heights[i] > heights[j]) {
        let temp = heights[i];
        heights[i] = heights[j];
        heights[j] = temp;
      }
    }
  }

  for (let i = 0; i < initHeights.length; i++) {
    if (initHeights[i] !== heights[i]) {
      count++;
    }
  }

  console.log(heights)
  return count;
}

// console.log(heightChecker([5,1,2,3,4]));
// console.log(heightChecker([1,1,4,2,1,3]));


function thirdFn(nums) {
  let hash = new Set(nums);
  let newArr = [...hash];
  for (let i = 0; i < newArr.length; i++) {
    for (let j = 0; j < newArr.length; j++) {
      if (newArr[i] > newArr[j]) {
        let temp = newArr[i];
        newArr[i] = newArr[j];
        newArr[j] = temp;
      }
    }
  }
  return newArr.length > 2 ? newArr[2] : newArr[0];
}

// console.log(thirdFn([3, 2, 1, 4]));
// console.log(thirdFn([1, 2, 2, 5, 3, 5]));
// console.log(thirdFn([1, 1, 2]));
// console.log(thirdFn([2, 2, 3, 1]));
// console.log(thirdFn([5, 2, 2]));

function findDisappearedNumbers(nums) {
  let result = [];

  for(let i = 0; i < nums.length; i++) {
    const index = Math.abs(nums[i]) - 1;
    if(nums[index] > 0) {
      nums[index] = -nums[index];
    }
  }

  for(let i = 0; i < nums.length; i++) {
    console.log(nums[i])
    if(nums[i] > 0) {
      result.push(i + 1);
    }
  }

  return result;
}

// console.log(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]));
console.log(findDisappearedNumbers([1, 2, 3, 3]));
// console.log(findDisappearedNumbers([1, 1]));
