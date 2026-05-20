# Time Delta Calculator

## Overview
The **Time Delta Calculator** is a Python program that calculates the absolute difference (in seconds) between two timestamps, even if they belong to different time zones.

This project solves the problem of comparing social media post timestamps shown in users’ news feeds when posts are published and viewed across different time zones.

---

## Problem Statement
When users post updates on social media (such as URLs, images, or status updates), other users in their network can view these posts on their news feed along with the time they were published (e.g., seconds, minutes, or hours ago).

Since users may be in different time zones, timestamps can differ even if they represent the same moment.

Given two timestamps in the format:

Day dd Mon yyyy hh:mm:ss +xxxx

Example:

Sun 10 May 2015 13:54:36 -0700

Your task is to calculate the **absolute difference in seconds** between the two timestamps.

---

## Input Format
- First line contains an integer **T** (number of test cases)
- Each test case contains:
  - First timestamp **t1**
  - Second timestamp **t2**

---

## Output Format
For each test case, print the **absolute difference in seconds**.

---

## Example

### Input
```text
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000