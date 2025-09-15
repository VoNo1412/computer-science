/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */

function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

var gcdOfStrings = function (str1, str2) {
    let lenGCD = gcd(str1.length, str2.length);
    let result = [];
    const candidate = str1.slice(0, lenGCD);

    for (let i = 0; i < str1.length; i += lenGCD) {
        let sameWord = str1.slice(i, i + lenGCD)
        if (sameWord == str2.slice(0, lenGCD) && candidate.repeat(str1.length / lenGCD) === str1 &&
            candidate.repeat(str2.length / lenGCD) === str2) {
            result.push(str1.slice(i, i + lenGCD));
        }
    }
    console.log(result)
    if (result.length >= 2) {
        return result[0];
    }
    return "";
};

// gcdOfStrings("ABCABC", "ABC"); // "ABC"
gcdOfStrings("ABABAB", "ABAB"); // "AB"
gcdOfStrings("AAAAAAAAA", "AAACCC"); // "ABC"
gcdOfStrings("ABCDEF", "ABC"); // "ABC"