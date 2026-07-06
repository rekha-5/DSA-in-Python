Largest Element in an Array
Problem Description
You are given an array of integers arr with size n. Your task is to find and return the largest element in the array.
Note: The largest element is the integer with the greatest numerical value among all elements in the array.
Difficulty
Easy
Example
Input:
text
n = 5
arr = [1, 8, 7, 56, 90]
Output:
text
90
Explanation:
The largest element in the given array is 90.
Constraints
Approach
Initialize a variable max_val with the first element of the array.
Iterate through the array starting from the second element.
If the current element is greater than max_val, update max_val.
Return max_val after the loop finishes.
Time Complexity: O(N)
Space Complexity: O(1)



