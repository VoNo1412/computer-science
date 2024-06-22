function pickFromBothSide(A, B) {
    const n = A.length;
    let leftSum = 0;
    let maxSum = 0;

    // Initialize left sum
    for (let i = 0; i < B; i++) {
      leftSum += A[i];
    }

    maxSum = leftSum;

    // Compute the sum from both ends
    for (let i = B - 1, j = n - 1; i >= 0; i--, j--) {
      leftSum -= A[i];
      leftSum += A[j];
      maxSum = Math.max(maxSum, leftSum);
    }

    return maxSum;
}

console.log(pickFromBothSide([5, -2, 3 , 1, 2], 3))
// console.log(pickFromBothSide([1, 2], 1))
// console.log(pickFromBothSide([ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ], 48))
