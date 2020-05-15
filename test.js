function solution(id_list, k) {
    var answer = 0;
    let coupon_count = {};

    for (let i = 0; i < id_list.length; i++) {
        let tran = new Set(id_list[i].split(' '));
        tran = [...tran];
        for (let j = 0; j < tran.length; j++) {
            const u = coupon_count[tran[j]];
            if (!u) {
                coupon_count[tran[j]] = 1;
            }
            else {
                if (u < k) {
                    coupon_count[tran[j]]++;
                }
            }
        }
    }

    for (let k in coupon_count) {
      answer += coupon_count[k];
    }
    console.log(coupon_count + ' ' + answer);
    return answer;
}

solution(["A B C D", "A D", "A B D", "B D"], 2);
solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3);
