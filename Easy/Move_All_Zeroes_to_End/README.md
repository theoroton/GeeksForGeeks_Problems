# 🌱 Problem : [Move All Zeroes to End](https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/0) 

**Difficulty :** Easy

## 🎯 Description :

You are given an array **arr[]** of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed **in place**, meaning you should not use extra space for another array.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
<strong>Output: </strong>[1, 2, 4, 3, 5, 0, 0, 0]
<strong>Explanation: </strong>There are three 0s that are moved to the end.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = [10, 20, 30]
<strong>Output: </strong>[10, 20, 30]
<strong>Explanation: </strong>No change in array as there are no 0s.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = [0, 0]
<strong>Output: </strong>[0, 0]
<strong>Explanation: </strong>No change in array as there are all 0s.
</span></pre>

## 🚧 Constraints

1 ≤ arr.size() ≤ 10<sup>5</sup>\
0 ≤ arr[i] ≤ 10<sup>5</sup>

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(1)