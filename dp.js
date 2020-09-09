function fibo(n) {
  if (n === 1) return 1
  if (n === 2) return 1
  if (arr[n] != undefined) return arr[n]
  arr[n] = fibo(n-1) + fibo(n-2)
  return arr[n]

}

var arr = []
console.log(fibo(50))

const a = 873465938416981340968734986
console.log(a)
