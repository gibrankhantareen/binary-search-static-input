# This code is for recursive binary search.
  
# By this code, it will return the index (position) of element 'x' in arrary if its present
# Let our element be X, 'half' be the half of the array

def binarySearch (array, length, half, x):  
    # Now we will check for base case
    if half >= length:
        array_ka_mid = length + (half - length) // 2
  
        # First we will check if our element is present at the Middle itself
        if array[array_ka_mid] == x:
            return array_ka_mid
          
        # Now if our element is 'smaller' than middle element, 
        # Then it will be present only in left subarray
        elif array[array_ka_mid] > x:
            return binarySearch(array, length, array_ka_mid-1, x)
  
        # Else if our element is 'bigger' than middle element,
        # Then it can only be present in Right subarray
        else:
            return binarySearch(array, array_ka_mid + 1, half, x)
  
    else:
        # Both cases are not satisfied, Thus our element is NOT present in the array
        return False
  
# Now lets give the Static input of the our sorted array
array = [ 1, 5, 8, 12, 56 ]
print("The Sorted Array is: ", array)
x = int(input("Enter your Element you which you want to find: "))
  
# Now we will call the Function to work upon input
result = binarySearch(array, 0, len(array)-1, x)
  
# The final result will be calculated by
if result != False:
    print ("Congratulations, your Element is present at index: ",result)
else:
    print ("Sorry your element is not present in array")