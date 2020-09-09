function quickSort(arr, start=0, end=arr.length-1) {
  if (start >= end) {
    return
  }

  const pivot = arr[start]
  let i = start + 1
  let j = end
  let temp

  while (i <= j) {
    while (arr[i] <= pivot) {     // 내림차순 변경부분1
      i++
    }
    while (arr[j] >= pivot && j > start) {    // 내림차순 변경부분2
      j--
    }
    if (i > j) {  // 엇갈림
      temp = arr[j]
      arr[j] = arr[start]
      arr[start] = temp
    } else {
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
    }
  }

  quickSort(arr, start, j - 1)
  quickSort(arr, j + 1, end)
}
// let arr = [5,2,3,1,4]
// quickSort(arr)
// console.log(arr)
