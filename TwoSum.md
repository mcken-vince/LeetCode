# Two Sum (easy)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Solutions written in Javascript. Quadratic-time algorithm: T(n) = O($n^2$).
```js
const twoSum = (nums, target) => {
    for (let num1 = 0; num1 < nums.length; num1++) {
        for (let num2 = 0; num2 < nums.length; num2++) {
            if (num2 === num1) {
                num2++;             
            }
            if (nums[num1] + nums[num2] === target) {
                return [num1, num2];
            }
        };
    };
};
```


The solution below works to get the correct numbers, but since the array 'nums' is sorted, the indices are changed and so it doesn't satisfy the test.
Linear-time algorithm: T(n) = O(n).
```js
const twoSum = (nums, target) => {
    nums.sort((a, b) => a - b);
    
    let low = 0;
    let high = nums.length - 1;

    while (high > low) {
        if (nums[low] + nums[high] === target) {
            return [low, high];
        } else if (nums[low] + nums[high] < target) {
            low++;
        } else if (nums[low] + nums[high] > target) {
            high--;
        }
    };
    return [];
};
```