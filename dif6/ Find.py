from operator import truediv


def find_uniq(arr):
    tab=arr
    while True:
        pom=tab.pop(0)
        if pom in arr:
            for i in range(len(arr)):
                if arr[0]!=arr[i]:
                    n=arr[i]
            break
        pom=tab.pop(1)

        if pom in arr:
            for i in range(len(arr)):
                if arr[1]!=arr[i]:
                    n=arr[i]
            break

        pom=tab.pop(2)       
        if pom in arr:
            for i in range(len(arr)):
                if arr[2]!=arr[i]:
                    n=arr[i]
            break
    return n  