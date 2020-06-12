# Roman Numeral to Integer

## Problem Description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

1. I can be placed before V (5) and X (10) to make 4 and 9. 
2. X can be placed before L (50) and C (100) to make 40 and 90. 
3. C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

---

## Input/Output

```
Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

For more cases, refer to `tests` directory.

---

## Test Instructions

1. Download pipenv for your environment e.g. `brew install pipenv` for MacOS users
2. Download project dependencies using `pipenv install --dev`
3. Run tests using `pipenv run python -m pytest`

## Test Coverage
1. Run `coverage run --source=. -m pytest`
2. Run `coverage html` to generate HTML report for coverage

---

## Learning Points

1. This is a good problem to practise writing unit tests. 
2. Unit tests should start from simplest cases, which test the return values for single characters. For example X returns 10, V returns 5 and so on.
3. We can then create more complex tests for the special logic for IX etc and different combinations of them.