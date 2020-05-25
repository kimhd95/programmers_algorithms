def solution(prices):
    answer = []

    for i in range(len(prices)-1):
        time = 0
        price = prices[i]
        for j in range(i+1, len(prices)):
            if price > prices[j]:
                time = j-i
                break;
        if time == 0:
            time = len(prices) - i - 1
        answer = answer + [time]
    answer = answer + [0]
    return answer
