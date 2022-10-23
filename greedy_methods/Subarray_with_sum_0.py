def findSubArrays(arr,n):
 
    # create a python dict
    hashMap = {}
     
    # create a python list
    # equivalent to ArrayList
    out = []
     
    # tracker for sum of elements
    sum1 = 0
    for i in range(n):
         
        # increment sum by element of array
        sum1 += arr[i]
         
        # if sum is 0, we found a subarray starting
        # from index 0 and ending at index i
        if sum1 == 0:
            out.append((0, i))
        al = []
         
        # If sum already exists in the map
        # there exists at-least one subarray
        # ending at index i with 0 sum
        if sum1 in hashMap:
             
            # map[sum] stores starting index
            # of all subarrays
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    return out
 
# print all subarrays with sum 0
def printOutput(arr,output):
    print("Number of subarrays with sum 0 = ",len(output))
    for i in output:
        print (arr[i[0]:i[1]+1])
 
def test():
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    n = len(arr)
    out = findSubArrays(arr, n)
     
    # if we did not find any subarray with 0 sum,
    # then subarray does not exists
    if (len(out) == 0):
        print ("No subarray exists")
    else:
        printOutput (arr,out)
test()
