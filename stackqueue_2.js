function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var ready = truck_weights;
    var cross = [];
    var cross_time = [];
    let time = 0;
    while (cross.length + ready.length > 0) {
        // 다 건넌 트럭 deq
        console.log("time: ", time);
        console.log(`cross: ${cross}    ready: ${ready}`);
        console.log("------------------------------------");
        if (cross_time.length > 0) {
          if (cross_time[0] + bridge_length === time) {
            cross.shift();
            cross_time.shift();
          }
        }

        // 건너는 트럭 enq
        let weight_sum = 0;
        for (let i = 0; i < cross.length; i++) {
            weight_sum += cross[i];
        }

        if (weight_sum + ready[0] <= weight) {
          cross.push(ready.shift());
          cross_time.push(time);
        }

        time++;
    }
    answer = time;
    return answer;
}

console.log(solution(2, 10, [7,4,5,6]));
