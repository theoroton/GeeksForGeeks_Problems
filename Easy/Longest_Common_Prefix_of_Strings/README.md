# 🌱 Problem : [Longest Common Prefix of Strings](https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/0) 

**Difficulty :** Easy

## 🎯 Description :

Given an array of strings **arr[]**. Return the **longest common prefix** among each and every strings present in the array. If there's no prefix common in all the strings, return "".

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
<strong>Output: </strong>"gee"
<strong>Explanation: </strong>"gee" is the longest common prefix in all the given strings.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>arr[] = ["hello", "world"]
<strong>Output: </strong>""
<strong>Explanation: </strong>There's no common prefix in the given strings.
</span></pre>

## 🚧 Constraints

1 ≤ |arr| ≤ 10<sup>3</sup>\
1 ≤ |arr[i]| ≤ 10<sup>3</sup>

## 🕒 Expected Complexities
**Time Complexity:** O(n*min(|arri|))\
**Auxiliary Space:** O(min(|arri|))