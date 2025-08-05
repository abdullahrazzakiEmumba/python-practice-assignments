def fibbonaci(arr,currentIdx,maxN):
    if currentIdx==maxN:
        return arr
    arr.append(arr[-1]+arr[-2])
    return fibbonaci(arr,currentIdx+1,maxN)
try:
    n = int(input("Enter how many numbers you want:"))
    print(fibbonaci([0,1],2,n))
except Exception as e:
    print(e)