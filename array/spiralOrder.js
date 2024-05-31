/**
 *  Step 1:
 * 
 *  Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
 */

const spiderRum = (arr) => {
    let newArr = [];

    let m = arr[0].length, n = arr.length;
    let last_row = n - 1, last_col = m - 1; 
    let k = 0, l = 0;

    while (k <= last_row && l <= last_col) {
        for (let i = l; i <= last_col; i++) {
            newArr.push(arr[k][i]);
        }
        k++;

        for (let i = k; i <= last_row; i++) {
            newArr.push(arr[i][last_col]);
        }
        last_col--;

        if (k <= last_row) {
            for (let i = last_col; i >= l; i--) {
                newArr.push(arr[last_row][i]);
            }
            last_row--;
        }

        if (l <= last_col) {
            for (let i = last_row; i >= k; i--) {
                newArr.push(arr[i][l]);
            }
            l++;
        }
    }

    return newArr;
}


console.log(spiderRum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]));

// console.log(spiderRum([
//     [1, 2],
//     [3, 4],
//     [5, 6]
//   ]))