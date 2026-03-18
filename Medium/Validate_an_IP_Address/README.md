# 🌱 Problem : [Validate an IP Address](https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/0) 

**Difficulty :** Medium

## 🎯 Description :

You are given a string **s** in the form of an IPv4 Address. Your task is to validate an **IPv4 Address**, if it is valid return **true** otherwise return **false**.

**IPv4 addresses** are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., "172.16.254.1"

A **valid IPv4 Address** is of the form x1.x2.x3.x4 where **0 <= (x1, x2, x3, x4) <= 255**. Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)

**Note:** Here we are considering numbers only from 0 to 255 and any additional **leading zeroes** will be considered invalid.

## 📝 Examples :

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "222.111.111.111"
<strong>Output: </strong>true
<strong>Explanation: </strong>Here, the IPv4 address is as per the criteria mentioned and also all four decimal numbers lies in the mentioned range.
</span></pre>

<pre><span style="font-size: 10pt;"><strong>Input: </strong>s = "5555..555"
<strong>Output: </strong>false
<strong>Explanation: </strong>"5555..555" is not a valid IPv4 address, as the middle two portions are missing.
</span></pre>

## 🚧 Constraints

1 ≤ |s| ≤ 15

## 🕒 Expected Complexities
**Time Complexity:** O(n)\
**Auxiliary Space:** O(1)