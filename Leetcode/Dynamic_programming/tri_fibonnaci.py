# dynamic programming
def tri_fibno(n, memo):
    if n <= 1:
        return n
    if n == 2:
        return 1
    
    if n in memo:
        return memo[n]
    else:
        result = tri_fibno(n-1, memo) + tri_fibno(n-2, memo) + tri_fibno(n-3, memo)
        memo[n] = result
    print(memo)
    return memo[n]
n = 29
memo = {}
print(tri_fibno(n, memo))
