/**
 * 
 * @param {*} explain: recursive call all and js add all factorial(5) factorial(4) factorial(3) ...  into stack;
 * when n === 0 then execute one by one factorial(5), factorial(4)....
 * @returns 
 */

function factorial(n) {
     if (n === 0) {
        return 1;
    }
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
}

console.log(factorial(5));