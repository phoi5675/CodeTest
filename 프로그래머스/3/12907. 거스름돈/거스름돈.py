def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지입니다.
    
    for coin in money:
        for j in range(coin, n+1):
            dp[j] += dp[j - coin]
            dp[j] %= 1_000_000_007  # 모듈러 연산으로 결과를 나눠줍니다.
    
    return dp[n]
