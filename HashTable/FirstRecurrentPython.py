"""
    Return a number which has 1st recurrent in an array
    Eg: [2,5,1,2,3,5,1,2,4] => return 2
    @args: arr[list] the array under search
    @return: num[int] the number with first recurrent
"""

arr = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 = [2,3,4,5]
arr4 = []
arr5 = None
def find_num_with_firstRecurrent(arr):
    """
    Return a number which has 1st recurrent in an array
    Eg: [2,5,1,2,3,5,1,2,4] => return 2
    
    Complexity : 
      - Time O(n) when last item is the first recurrent,
      - Mem O(n) n when no identical items
    @args: arr[list] the array under search
    @return: num[int] the number with first recurrent
    """
    if arr == None:
        return None
    #create log table for pairs of value:ocurrence
    logTable = {}
    num = None
    #put in the table
    for a in arr:
        logTable[a] = None
    #if value occurs twice then return value
    for a in arr:
        print("Num a" + str(a))
        if logTable[a] == None: #first time occurs
            print("Num a 1st time" + str(a))
            logTable[a] = 1 
        elif logTable[a] == 1: #second time occurs
            print("Num a 2nd time" + str(a))
            num = a
            break

    return num
if __name__ == "__main__":
    num = find_num_with_firstRecurrent(arr5)
    print(num)
            
        
        

        
