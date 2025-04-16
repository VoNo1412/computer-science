function diagonalSum(mat) {
    let total = 0;
    let n = mat.length
    for (let i = 0; i < mat.length; i++) {
        total += mat[i][i] + mat[i][n - 1 - i];
        if (n % 2 !== 0 && i == Math.floor(n /2)) {
            total -= mat[i][i];
        }
    }
    return total;
}

let result = diagonalSum([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

console.log(result)