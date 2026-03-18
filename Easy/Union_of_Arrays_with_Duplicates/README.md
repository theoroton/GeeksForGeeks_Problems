# 🌱 Problem : [Union of Arrays with Duplicates](https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/0) 

**Difficulty :** Easy

## 🎯 Description :

You are given two arrays **a[]** and **b[]**, return the **Union** of both the arrays in any order.

The **Union** of two arrays is a collection of all **distinct elements** present in either of the arrays. If an element appears more than once in one or both arrays, it should be included **only once** in the result.

**Note:** Elements of **a[]** and **b[]** are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in **sorted order** only.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
<strong>Output: </strong>[1, 2, 3]
<strong>Explanation: </strong>Union set of both the arrays will be 1, 2 and 3.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>a[] = [1, 2, 3], b[] = [4, 5, 6] 
<strong>Output: </strong>[1, 2, 3, 4, 5, 6]
<strong>Explanation: </strong>Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1]
<strong>Output: </strong>[1, 2]
<strong>Explanation: </strong>Union set of both the arrays will be 1 and 2.
</span></pre>

## 🚧 Constraints

1 ≤ a.size(), b.size() ≤ 10<sup>6</sup>\
0 ≤ a[i], b[i] ≤ 10<sup>5</sup>

## 🕒 Expected Complexities
**Time Complexity:** O(n + m)\
**Auxiliary Space:** O(n + m)