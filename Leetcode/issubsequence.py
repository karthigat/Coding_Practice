def subseuence(str1, str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i+=1
        j+=1
    return True if i == len(str1) else False
      

str1 = "axb"
str2 = "ahbgdc"
print(subseuence(str1, str2))