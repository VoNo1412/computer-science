class Sort {
    bubbleSort(array) {
        for (let i = 0; i < array.length; i++) {
            for (let j = 0; j < array.length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    [array[j], array[j + 1]] = [array[j + 1], array[j]];
                }
            }
        }
    }

    selectionSort(array) {
        for (let i = 0; i < array.length; i++) {
            let lowestIdx = i;

            for (let j = i + 1; j < array.length; j++) {
                if (array[lowestIdx] > array[j]) {
                    lowestIdx = j;
                }
            }

            if (lowestIdx != i) {
                [array[lowestIdx], array[i]] = [array[i], array[lowestIdx]];
            }
        }
    }

    insertionSort(array) {
        for (let i = 1; i < array.length; i++) {
            let current = array[i];
            let j = i - 1;

            while (j >= 0 && array[j] > current) {
                array[j + 1] = array[j];
                j--;
            }

            array[j + 1] = current;
        }
    }
}

let sort = new Sort();
let arr = [5, 3, 8, 4, 2];
sort.insertionSort(arr);
console.log(arr); // Output: [2, 3, 4, 5,