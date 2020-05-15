function solution(baseball) {
    var answer = 0;
    const cases = []
    for (let a=1; a < 10; a++) {
      for (let b=1; b < 10; b++) {
        for (let c=1; c < 10; c++) {
          if (!(a==b || a==c || b==c)) {
            let num = a.toString() + b.toString() + c.toString();
            cases.push(num);
          }
        }
      }
    }

    for (q in baseball) {
      
    }

    console.log(cases);
    return answer;
}
solution()
