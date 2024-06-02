def maximum_vowles(s, k):
    i = k
    maximum = 0
    max_vowles = 0
    vowles = ['a','e','i','o','u']
    for i in range(k):
        if s[i] in vowles:
            max_vowles += 1
    maximum = max(maximum, max_vowles)
    for j in range(k, len(s)):
        if s[j] in vowles:
            max_vowles += 1
        if s[j-k] in vowles:
            max_vowles -= 1
        maximum = max(maximum, max_vowles)
    return maximum


s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
k = 33
print(maximum_vowles(s,k))