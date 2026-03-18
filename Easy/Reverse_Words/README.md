# 🌱 Problem : [Reverse Words](https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/0) 

**Difficulty :** Easy

## 🎯 Description :

Given a string **s**, **reverse** the string without reversing its **individual words**. Words are separated by **dots(.)**.

**Note:** The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words, and **no extra dots** should be included.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "i.like.this.program.very.much"
<strong>Output: </strong>"much.very.program.this.like.i"
<strong>Explanation: </strong>The words in the input string are reversed while maintaining the dots as separators, resulting in "much.very.program.this.like.i".
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "..geeks..for.geeks."
<strong>Output: </strong>"geeks.for.geeks"
<strong>Explanation: </strong>After removing extra dots and reversing the whole string, the input string becomes "geeks.for.geeks".
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "..home....."
<strong>Output: </strong>"home"
<strong>Explanation: </strong>The input string contains only one word with extra dots around it. After removing the extra dots, the output is "home".
</span></pre>

## 🚧 Constraints

1 ≤ s.length() ≤ 10<sup>6</sup>\
String **s** contains only lowercase English alphabets and dots.

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(1)