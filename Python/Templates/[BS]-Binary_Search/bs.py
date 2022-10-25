##### Binary Search Algorithm Implementation
### Implementation Author:  pashka codeforces
### Time Complexity:        O(log n)
### github.com/mttgermano

### [24/10/2022] [v1.0]
### Release Notes:
# Answer is 0-index
# All functions working well!


###Binary Search
# Exact element
def bs(list,element):
    l = -1
    r = len(list)

    while r >= l:
        m = (l+r)//2

        # Exect element 
        if list[m] == element:
            return m
        elif list[m] < element:
            l = m + 1
        elif list[m] > element:
            r = m - 1
    return -1


###Upper_Bound Binary Search
# Exect element xor Upper_bound 
def bsu(list,element):
    l = -1
    r = len(list)

    while r > l+1:
        m = (l+r)//2

        if list[m] <= element:
            l = m
        else:
            r = m
    return r


###Lower_Bound Binary Search
# Exect element xor Lower_bound 
def bsl(list,element):
    l = -1
    r = len(list)

    while r > l+1:
        m = (l+r)//2

        if list[m] <= element:
            l = m
        else:
            r = m
    return l