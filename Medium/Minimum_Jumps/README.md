# 🌱 Problem : [Minimum Jumps](https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/0) 

**Difficulty :** Medium

## 🎯 Description :

You are given an array **arr[]** of non-negative numbers. Each number tells you the **maximum number of steps** you can jump forward from that position.

For example:
- If **arr[i] = 3**, you can jump to index **i + 1**, **i + 2**, or **i + 3** from position **i**.
- If **arr[i] = 0**, you **cannot jump forward** from that position.

Your task is to find the **minimum number of jumps** needed to move from the **first** position in the array to the last position.

**Note:**  Return **-1** if you can't reach the end of the array.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
<strong>Output: </strong>3
<strong>Explanation: </strong>First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr = [1, 4, 3, 2, 6, 7]
<strong>Output: </strong>2
<strong>Explanation: </strong>First we jump from the 1st to 2nd element and then jump to the last element.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr = [0, 10, 20]
<strong>Output: </strong>-1
<strong>Explanation: </strong>We cannot go anywhere from the 1st element.
</span></pre>

## 🚧 Constraints
2 ≤ arr.size() ≤ 10<sup>5</sup>\
0 ≤ arr[i] ≤ 10<sup>5</sup>

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(1)