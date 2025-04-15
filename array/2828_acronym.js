/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function (words, s) {
    let str = "";
    words.forEach(x => str += x.charAt(0));
    return str == s;
};

// let words = ["never","gonna","give","up","on","you"], s = "ngguoy"
// let words = ["an", "apple"], s = "a"
words = ["ekin","f","rabj","driadwjqz"], s = "defr"

let result = isAcronym(words, s)
console.log(result);