function solution(priorities, location) {
    let order = 1;
    let loc = location;

    const queue = priorities;

    while (queue.length > 0) {
      // console.log(queue);
      let pr = queue.shift();
      if (loc == 0) {   // 꺼낸 게 내 문서면
        if (pr < max(queue)) {
          queue.push(pr);
          loc = queue.length - 1;
        } else {
          break;
        }
      } else {
        if (pr < max(queue)) {
          queue.push(pr);
        } else {
          order++;
        }
        loc--;
      }
    }

    console.log(order);
    return order;
}

function max(arr) {
  return Math.max.apply(null, arr);
}

solution([2, 1, 3, 2], 2)
