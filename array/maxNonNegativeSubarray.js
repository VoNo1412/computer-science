function maxNonNegativeSubArray(arr) {
    let max = 0, newArr = [], sub = [];
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] > -1) {
            sub.push(arr[i]);
        } else {
            newArr.push(sub);
            sub = [];
        }

        if(i === arr.length - 1) {
            newArr.push(sub);
        }
    }

    for (let sublist1 of newArr) {
        let total = 0;
        for (let sublist2 of sublist1) {
            total += sublist2;
        }
        
        if(total === 0 && max < sublist1.length) {
            max = sublist1.length;
            sub = sublist1;
        }

        if(max < total) {
            max = total;
            sub = sublist1
        }

    }
    return sub;
}


console.log(maxNonNegativeSubArray([1, 2, 5, -7, 2, 3]));
console.log(maxNonNegativeSubArray([10, -1, 2, 3, -4, 100]));
console.log(maxNonNegativeSubArray([ 0, 0, -1, 0 ]));