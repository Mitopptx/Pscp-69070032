# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3024/S
```

OJ submission ID, if submitted:

```text
550898
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
3-6 hours
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
Input two values the total score and the highest score. The program will check if the difference between the highest score and the lowest score is not more than 2.
```
---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: Calculating the lowest score by assuming the second score was one point lower than the highest score. Then I used the remaining score as the lowest score but this method did not work.
Step 2: I tried using percentages. I calculated the highest possible score if it more than 36% It's mean the difference between the highest and lowest scores would be more than 2 it's still in correct
Step 3: So I wrote many test cases one by one. I noticed a pattern. Every time the total score was three points lower than the maximum possible total, the difference between the highest and lowest scores became greater than 2. From this pattern, I found the formula (highest score × 3) − 2 Ex the highest score is 10 | (10 × 3) − 2 = 28
If the total score is less than 28, the difference between the highest and lowest scores is greater than 2, so it exceeds the limit.

the test case i wrote down
30 10 10 10
29 10 10 9
28 10 10 8 | 10 9 9
27 10 10 7 | 10 9 8
         ^ exceed ^ not exceed
26 10 10 6 | 10 9 7 | 10 8 8
         ^ exceed ^ exceed ^ not exceed


OR

27 9 9 9                              24  8 8 8
26 9 9 8                              23  8 8 7
25 9 9 7 | 9 8 8                      22  8 8 6 | 8 7 7
24 9 9 6 | 9 8 7                      21  8 8 5 | 8 7 6
       ^ exceed                               ^ exceed
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
I did not ask anyone or use AI because I was too lazy to write an AI submission report so I solved the problem on my own.
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
In my first atempt I got this testcase wrong becasuse it's can be 10 10 7 or 10 9 8
```

Input:

```text
27
10
```

Expected output:

```text
surprising
```

Actual output:

```text
surprising
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
I had a problem when calculating the percentage because of zero.
```

Input:

```text
1
0
```

Expected output:

```text
Not Surprising
```

Actual output:

```text
Not Surprising
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
If the input has low values such as 0 1 2 ( 3 when the highest score is 2), the result should be "not surprise." However, my program calculated a negative number, so it gave the wrong result.
```

Input:

```text
2
1
```

Expected output:

```text
Not Surprising
```

Actual output:

```text
Not Surprising
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text
myself, my brain and my boba tea
```

What did they help with?

```text
think
```

What did you still do by yourself?

```text
do my best
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes|
| I understand my final code. | Yes|
| I recorded the real OJ status. |Yes |
| I did not copy AI-generated text directly into this file. | Yes|
| I did not copy code from another person. |Yes |
| If I received human help, I disclosed it in this file. |Yes |
| I submitted the final code to the OJ by myself. |Yes |
