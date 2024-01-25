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

def sumArray(array):
    biggestSum = 0
    currentSum = 0
    
    for num in range(len(array)):
    
        if num + 1 < len(array) and (array[num] + array[num + 1]) > biggestSum:
            currentSum = array[num] + array[num + 1]
            biggestSum = currentSum
            if num - 1 > len(array) and currentSum < currentSum + array[num - 1]:
                currentSum = currentSum + array[num - 1]
                biggestSum = currentSum
            
        if biggestSum < currentSum:
            biggestSum = currentSum   
        currentSum = 0    
                   
    return biggestSum

print(sumArray([1, -2, 3, 10, -4, 7, 2, -5]))       #[3, 10, -4, 7, 2]-> 18
"""The idea is to iterate through the array, keeping track of the current sum and
updating it based on whether adding the next element increases the sum or not.
The maximum sum encountered during the iteration will be the answer."""