def container(heights):
    #container_volue = height(min of two indexes) * width (between indexes)
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        area = (r-l) * min(height[r], height[l])
        max_area= max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


height = [1,1]
print(container(height))