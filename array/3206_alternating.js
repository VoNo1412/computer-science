/**
 * @param {string} s
 * @return {string}
 */
var smallestPalindrome = function (s) {
    let countWord = new Map();

    [...s].forEach(x => {
        countWord.set(x, (countWord.get(x) || 0) + 1);
    });
    let result = [];

    // Sắp xếp các ký tự theo thứ tự alphabet
    let sortedChars = [...countWord.keys()].sort();

    let middle = ""; // Biến lưu trữ phần giữa nếu có ký tự lẻ

    for (let char of sortedChars) {
        let count = countWord.get(char);
        // Thêm nửa số lần xuất hiện của ký tự vào phần trái
        if (Math.floor(count / 2) > 0) {
            result.push(char.repeat(Math.floor(count / 2)));
        }
        // Nếu có ký tự có số lần lẻ, thì phần giữa sẽ là ký tự đó
        if (count % 2 !== 0) {
            middle = char;
        }
    }

    // Tạo phần bên phải bằng cách đảo ngược phần trái
    let rightHalf = [...result].reverse();

    // Nếu độ dài chuỗi là chẵn, không cần phần giữa
    if (s.length % 2 === 0) {
        middle = "";
    }

    // Ghép lại phần trái, phần giữa, và phần phải để tạo palindrome
    let palindrome = result.join('') + middle + rightHalf.join('');
    return palindrome;
};

let result = smallestPalindrome("rur") // acddca
// let result = smallestPalindrome("babab")
console.log(result)