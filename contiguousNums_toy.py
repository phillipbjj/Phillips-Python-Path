""" * Given an array of numbers, calculate the greatest contiguous sum of numbers in it.
 * A single array item will count as a contiguous sum.
 * example 1: sumArray([""1, 2, 3 ""]); // => 6
 * example 2: sumArray([""1, 2, 3"", -4]); // 6
 * example 3: sumArray([""1, 2, 3, -4, 5""]); // 7
 * example 4: sumArray([""4, -1, 5""]); // => 8
 * example 5: sumArray([10, -11, ""11""]); // 11
// Solved in O(n) time with O(1) memory
var sumArray = function(array) {
};"""
#num + 1 < len(array) and num - 1 > len(array) and
def sumArray(array):
    biggestSum = array[0]
    currentSum = array[0]

    for num in array[1:]:
        if currentSum + num > num:
            currentSum = currentSum + num
        else:
            currentSum = num

        if currentSum > biggestSum:
            biggestSum = currentSum
        
    return biggestSum  

print(sumArray([1, -2, 3, 10, -4, 7, 2, -5]))       #[3, 10, -4, 7, 2]-> 18
"""The idea is to iterate through the array, keeping track of the current sum and
updating it based on whether adding the next element increases the sum or not.
The maximum sum encountered during the iteration will be the answer."""

"""currentSum is the maximum sum ending at the current position.
biggestSum is the maximum sum we’ve seen so far.
For each number in the array (starting from the second number), we update currentSum to be the current number if the sum of the current number and 
the previous currentSum is less than the current number. Otherwise, we add the current number to currentSum.
If currentSum is larger than biggestSum, we update biggestSum.
Finally, we return biggestSum which is the largest contiguous sum in the array.
This approach ensures that we’re always considering the largest sum that includes the current number, and we keep track of the largest sum we’ve seen so far."""
