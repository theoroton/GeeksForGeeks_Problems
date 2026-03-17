# 🌱 Problem : [Parenthesis Checker](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1) 

**Difficulty :** Easy

## 🎯 Description :

Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is **balanced** or not.
An expression is balanced if:
1. Each opening bracket has a corresponding closing bracket of the same type.
2. Opening brackets must be closed in the correct order.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "[{()}]"
<strong>Output: </strong>true
<strong>Explanation: </strong>All the brackets are well-formed.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "[()()]{}"
<strong>Output: </strong>true
<strong>Explanation: </strong>All the brackets are well-formed.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "([]"
<strong>Output: </strong>false
<strong>Explanation: </strong>The expression is not balanced as there is a missing ')' at the end.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "([{]})"
<strong>Output: </strong>false
<strong>Explanation: </strong>The expression is not balanced as there is a closing ']' before the closing '}'.
</span></pre>

## 🚧 Constraints

1 ≤ s.size() ≤ 10<sup>6</sup>\
s[i] ∈ {'{', '}', '(', ')', '[', ']'}

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(n)