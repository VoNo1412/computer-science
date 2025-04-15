/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let maxNum = 0;

    sentences.forEach(x => {
        let num = x.split(" ").length;
        maxNum = Math.max(num, maxNum)
    })

    return maxNum;
};

let result = mostWordsFound( ["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
console.log(result)