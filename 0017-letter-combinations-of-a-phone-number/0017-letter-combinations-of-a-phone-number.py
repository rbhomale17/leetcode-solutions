class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        def backtrack(index, current_string):
            # print(f"curr_str: {current_string} & index: {index}")
            if len(current_string) == len(digits):
                result.append(current_string)
                return
            current_digit = digits[index]
            # print(current_digit)
            for char in digit_mapping[current_digit]:
                # print(char)
                backtrack(index+1, current_string+char)

        backtrack(0, "")

        return result


print("""
## Time Complexity (TC)

1. Key observation

   * Each digit maps to a set of letters:

     * Digits 2–6, 8 → 3 letters each
     * Digits 7 and 9 → 4 letters each
   * Suppose the input string `digits` has length `n`.

2. How many combinations are possible?

   * If all digits mapped to 3 letters → 3ⁿ combinations
   * In the worst case (if all were 7s or 9s) → 4ⁿ combinations
   * More generally → O(4ⁿ) in worst case, O(3ⁿ) in best case.

3. Work per combination

   * Constructing each string costs O(n) because strings are immutable in Python (concatenating `current_string + char` creates a new string each time).

4. Final worst-case TC

   O(k^n * n)

   where:

   * `n` = length of `digits`
   * `k` = maximum number of letters for any digit (≤ 4)

   In worst case:

   O(4^n * n)


---

## Space Complexity (SC)

1. Recursion stack

   * Maximum recursion depth = `n`
   * Each call stores `current_string` (length up to `n`) → O(n) space.

2. Result storage

   * Number of results = O(kⁿ) strings, each of length n → O(n · kⁿ) space.

3. Digit mapping dictionary

   * Constant size → O(1).

Final SC:

O(n * k^n)

because the output list dominates memory usage.

---

Summary:

Time Complexity: O(4ⁿ · n) worst case
Space Complexity: O(n · 4ⁿ) worst case (due to storing all combinations)
""")

