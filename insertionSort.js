function insertionSort(arr) {
  let i, j, temp
  for (i = 0; i < arr.length; i++) {
    let j = i
    while (j >= 0 && arr[j] > arr[j+1]) {
      // SWAP
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
      j--
    }
  }
}

// let arr = [1,10,5,7,8,2,4,6,3,3,9]
//
// insertionSort(arr)
// console.log(arr)
