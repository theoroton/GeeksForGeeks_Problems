# 🌱 Problem : [Segregate 0s and 1s](https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/0) 

**Difficulty :** Easy

## 🎯 Description :

Given an array **arr** consisting of only **0**'s and **1**'s in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = [0, 0, 1, 1, 0]
<strong>Output: </strong>[0, 0, 0, 1, 1]
<strong>Explanation: </strong>After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = [1, 1, 1, 1]
<strong>Output: </strong>[1, 1, 1, 1]
<strong>Explanation: </strong>There are no 0s in the given array, so the modified array is [1, 1, 1, 1]
</span></pre>

## 🚧 Constraints

1 ≤ arr.size() ≤ 10<sup>6</sup>\
0 ≤ arr[i] ≤ 1

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(1)