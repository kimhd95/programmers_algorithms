function isPrime(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) return false
  }
  return true
}


function eratosthenesSeive(n) {
  let arr = [null, null]
  for (let i = 2; i <= n; i++) {
    arr[i] = i
  }
  for (let i = 2; i <= n; i++) {
    if (!arr[i]) continue
    for (let j = 2*i; j <= n; j+=i) {
      arr[j] = null
    }
  }
  arr = arr.filter(x => x)
  return arr
}
