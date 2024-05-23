class Solution(object):
    def reverse(self, x):
        d = 0
        negative = False
        if (x < 0):
            negative = True
        x = abs(x)
        while(x):
            #print(x)
            a = int(x%10)
            #print(a)
            d = (d*10) + a
            #print(d)
            x = int(x/10)

            if d > 0x7FFFFFFF:
                return 0
            #print(x)
        return d if not negative else -1*d
y = Solution()
t= -153423646
print(y.reverse(t))
