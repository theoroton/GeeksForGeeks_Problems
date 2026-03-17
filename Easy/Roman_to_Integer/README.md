# 🌱 Problem : [Roman to Integer](https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/0) 

**Difficulty :** Easy

## 🎯 Description :

Given a string s in Roman number format, your task is to **convert** it to an **integer**. Various symbols and their values are given below.\
**Note:** I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "IX"
<strong>Output: </strong>9
<strong>Explanation: </strong>IX is a Roman symbol which represents 10 – 1 = 9.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "XL"
<strong>Output: </strong>40
<strong>Explanation: </strong>XL is a Roman symbol which represents 50 – 10 = 40.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "MCMIV"
<strong>Output: </strong>1904
<strong>Explanation: </strong>M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.
</span></pre>

## 🚧 Constraints

1 ≤ roman number ≤ 3999\
s[i] ∈ [I, V, X, L, C, D, M]

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(1)