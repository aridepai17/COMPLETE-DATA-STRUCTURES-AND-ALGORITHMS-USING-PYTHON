samplearray = [ 5, 4, 10, 34, 2, 32, 56, 877, 325, 5444, 132, 33, 89]

def findbiggestnumber(samplearray):
    biggestnumber = samplearray[0] # O(1)
    for index in range(1, len(samplearray)): # O(n)
        if samplearray[index] > biggestnumber: # O(1)
            biggestnumber = samplearray[index] # O(1)

    return biggestnumber # O(1)

# Time Complexity = O(1) + O(n) + O(1) = O(n)