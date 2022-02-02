# LeetCode submission for TwoSum problem
## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the _two numbers_ such that they add up to `target`.

You may assume that each input would have **_exactly one solution_**, and you may not use the same element twice.

You can return the answer in any order.

## My Solution
Average runtime: 600 - 700ms
<br>
Average memory usage: 14MB
- For every integer, `value` in the `nums` list, subtract it from the `target` integer to get a `remainder` integer
- Using the `remainder` integer, search the remainder of the `nums` list for a matching integer
- Return the indices of `value` and `remainder`

## Best Solution On Leetcode
Average runtime: 60 - 100ms
<br>
Average memory usage: 14MB
- Create a dictionary / hashmap called `seen` to store past indices (as a value) and `value` (as the corresponding key) from the `nums` list 
- For every integer, `value` in the `nums` list, subtract it from the `target` integer to get a `remainder` integer
- Search the `seen` hashmap keys for a `value` key that matchings the value of `remainder` and return the corresponding value (index in `nums` list)
- If the `value` key is not found using the `remainder`, store the current `value` as a key to the current index 

## Analysis
- Using a hashmap to store a record of past values and indices **"seen"** by the programme helps reduce time spent searching the remainder of the `nums` list
