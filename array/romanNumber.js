/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const romanNumber = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };


    if (!s.length) return 0;
    if (s.length === 1)  return romanNumber[s[0]];

    if (romanNumber[s[0]] < romanNumber[s[1]]) {
        return (romanNumber[s[1]] - romanNumber[s[0]]) + romanToInt(s.slice(2));
    } else {
        return romanNumber[s[0]] + romanToInt(s.slice(1));
    }
};

// console.log(romanToInt("MCMXCIV")); // 1994
console.log(romanToInt("LVIII"));
console.log(romanToInt("III")); // 58

