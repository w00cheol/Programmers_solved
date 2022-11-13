def solution(strs, t):
    dp = [0]
    strs = set(strs)

    for i in range(len(t)):
        m_answer = 2e9
        
        for j in range(max(0, i-5), i+1):
            if t[j:i+1] in strs:
                m_answer = min(m_answer, dp[j] + 1)
        
        dp.append(m_answer)

    return dp[-1] if dp[-1] < 2e9 else -1 