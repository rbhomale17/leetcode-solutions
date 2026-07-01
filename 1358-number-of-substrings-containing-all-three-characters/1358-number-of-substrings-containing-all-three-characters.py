class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        last_seen = {"a": -1, "b": -1, "c": -1}
        # {"a": 0, "b": 1, "c": 2}
        for i in range(n):
            last_seen[s[i]] = i
            if (
            last_seen["a"] != -1 
            and last_seen["b"] != -1 
            and last_seen["c"] != -1
            ):
                left = min(last_seen["a"], last_seen["b"], last_seen["c"])
                res += left + 1
                # res = 1
        return res


