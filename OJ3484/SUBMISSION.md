# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3484/หุ่นยนต์เคาะเสียงกระเบื้อง
```

OJ submission ID, if submitted:

```text
666365
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
Inputing an N × N grid, where each value represents the number of defective tapping points on that tile (0–5).
then Print the grid, then add the number of defective tiles and number of defective points for each row.
Print the same two totals for each column.
Finally, print the total defective tiles, total defective points, and total penalty (defective points × P) with 2 decimal places.
---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: Read the N × N grid and create arrays to store the number of defective tiles and defective points for each row and column.
Step 2: Go through each value in the grid. Count defective tiles (j != 0), add the defective points to the corresponding column, and count defective tiles in each column.
Step 3: Print the grid with row totals, then print the column totals. Finally, calculate and print the total defective tiles, total defective points, and total penalty.
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
asked TA why EOF ERROR and they explain that I +k in the start of loop so it's go in first index instead of 0
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
All zeros
```

Input:

```text
3 100
0 0 0
0 0 0
0 0 0
```

Expected output:

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 
0 0 0 
0 0 0.00
```

Actual output:

```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 
0 0 0 
0 0 0.00
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
Different values in every position
```

Input:

```text
4 50
1 2 3 4
5 0 1 2
2 4 0 5
3 1 5 0
```

Expected output:

```text
1 2 3 4 4 10
5 0 1 2 3 8
2 4 0 5 3 11
3 1 5 0 3 9
4 3 3 3
11 7 9 11
13 38 1900.00
```

Actual output:

```text
1 2 3 4 4 10
5 0 1 2 3 8
2 4 0 5 3 11
3 1 5 0 3 9
4 3 3 3
11 7 9 11
13 38 1900.00
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
Many defective tiles but different point counts
```

Input:

```text
5 125
5 0 1 0 3
0 2 0 4 0
1 1 5 2 3
0 5 0 1 4
2 0 3 0 5
```

Expected output:

```text
5 0 1 0 3 3 9
0 2 0 4 0 2 6
1 1 5 2 3 5 12
0 5 0 1 4 3 10
2 0 3 0 5 3 10
3 3 3 3 4
8 8 9 7 15
16 47 5875.00
```

Actual output:

```text
5 0 1 0 3 3 9
0 2 0 4 0 2 6
1 1 5 2 3 5 12
0 5 0 1 4 3 10
2 0 3 0 5 3 10
3 3 3 3 4
8 8 9 7 15
16 47 5875.00
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
asked TA why EOF ERROR and they explain that I +k in the start of loop so it's go in first index instead of 0
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
no one
```

What did they help with?

```text
nothing
```

What did you still do by yourself?

```text
everything
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
| I recorded the real OJ status. | Yes|
| I did not copy AI-generated text directly into this file. | Yes|
| I did not copy code from another person. | Yes|
| If I received human help, I disclosed it in this file. | Yes|
| I submitted the final code to the OJ by myself. | Yes|
