/*
퀵정렬보다 빠르지는 않지만 항상 O(nlogn)을 보장.

병합정렬을 수행할 배열은 전역변수로 선언해야함

메모리에서 비효율적
*/
var sorted = []

function mergeSort(arr, i1, i2) {
  if (i1 < i2) {
    const m = Math.floor((i1 + i2) / 2)
    mergeSort(arr, i1, m)
    mergeSort(arr, m+1, i2)
    merge(arr, i1, m, i2)
  }
}

function merge(arr, i1, m, i2) {
  let i = i1
  let j = m + 1
  let k = i1

  while (i <= m && j <= i2) {
    if (arr[i] <= arr[j]) {
      sorted[k] = arr[i]
      i++
    } else {
      sorted[k] = arr[j]
      j++
    }
    k++
  }

  if (i > m) {
    for (let l = j; l <= i2; l++) {
      sorted[k] = arr[l]
      k++
    }
  } else {
    for (let l = i; l <= m; l++) {
      sorted[k] = arr[l]
      k++
    }
  }

  for (let l = m; l <= i2; l++) {
    arr[l] = sorted[l]
  }
}

const arrr = [78,6,3,4,1]
mergeSort(arrr, 0, arrr.length - 1)
console.log(arrr)
