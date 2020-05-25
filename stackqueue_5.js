function solution(arrangement) {
    let overlapped = 0;
    let count = 0;
    for (let i = 0; i < arrangement.length; i++) {
      const cur = arrangement[i];
      if (cur == '(') {
        if (isLaser(arrangement, i)) {
          count += overlapped;
        } else {
          overlapped++;
        }
      } else {  // ')'
        if (!isLaser(arrangement, i)) {
          overlapped--;
          count++;
        }
      }
    }
    // console.log(count);
    return count;
}

function isLaser(arrangement, index) {
  if (arrangement[index] == ')') {
    return arrangement[index - 1] == '(';
  } else {
    return arrangement[index + 1] == ')';
  }
}

// solution("()(((()())(())()))(())");
