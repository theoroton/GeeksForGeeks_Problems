# 🌱 Problem : [Parenthesis Checker](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1) 

**Difficulty :** Easy

## 🎯 Description :

Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is **balanced** or not.
An expression is balanced if:
1. Each opening bracket has a corresponding closing bracket of the same type.
2. Opening brackets must be closed in the correct order.

## 📝 Examples :

> **Input:** s = "[{()}]"\
> **Output:** true\
> **Explanation:** All the brackets are well-formed.

> **Input:** s = "[()()]{}"\
> **Output:** true\
> **Explanation:** All the brackets are well-formed.

> **Input:** s = "([]"\
> **Output:** false\
> **Explanation:** The expression is not balanced as there is a missing ')' at the end.

> **Input:** s = "([{]})"\
> **Output:** false\
> **Explanation:** The expression is not balanced as there is a closing ']' before the closing '}'.

## 🚧 Constraints

1 ≤ s.size() ≤ 10<sup>6</sup>\
s[i] ∈ {'{', '}', '(', ')', '[', ']'}

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(n)