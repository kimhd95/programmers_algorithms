function solution(numbers, target) {
    var answer = 0;
    console.log("123143134");
    dfs(0);

    return answer;
}

function dfs(n) {
  console.log(12321434);
  console.log(n);
    if (n === numbers.length) {
        let sum = 0;
        for (let i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        console.log("N: ", n);
        console.log("sum: ", sum);
        if (sum === target) {
            answer++;
        }
    }
    else {
        dfs(n+1);
        numbers[n] *= -1;
        dfs(n+1);
    }
}
