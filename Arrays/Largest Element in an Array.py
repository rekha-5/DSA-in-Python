class solution:
    def largestElement(self, arr, n):
        #Write your code here...
        max_element=arr[0]
        for i in range(1,n-1):
            if(arr[i]>max_element):
                max_element=arr[i]
        return max_element
        
    
       
