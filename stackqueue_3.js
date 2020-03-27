function solution(progresses, speeds) {
    var answer = [];
    let prog = progresses;
    let spd = speeds;
    while (prog.length > 0) {
      prog = prog.map((val, index) => {
        return val+spd[index];
      });

      let count = 0;
      for (let i = 0; i < prog.length; i++) {
        if (prog[i] >= 100) {
          count = i+1;
        } else {
          break;
        }
      }
      for (let j = 0; j < count; j++) {
        prog.shift();
        spd.shift();
      }
      if (count > 0) {
        answer.push(count);
      }
      // console.log(prog);
      // console.log("---------------");
    }

    // console.log(answer);
    return answer;
}
// solution([93,30,55], [1,30,5]);
