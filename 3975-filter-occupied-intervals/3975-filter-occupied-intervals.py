class Solution:
    def filterOccupiedIntervals(
        self,
        occupiedIntervals: List[List[int]],
        freeStart: int,
        freeEnd: int
    ) -> List[List[int]]:

        if not occupiedIntervals:
            return []

        # Sort the occupied intervals by start time.
        occupiedIntervals.sort()

        merged = [occupiedIntervals[0]]
        # Merging intervals
        for start, end in occupiedIntervals:
            last = merged[-1]

            # add + 1 here to handle adjacent interval [[1,2],[3,6]]
            if last[1] + 1 >= start:
                last[1] = max(last[1], end)
            else:
                merged.append([start, end])

        return self.split(merged, freeStart, freeEnd)

    def split(self, intervals, freeStart, freeEnd):
        """
        After merging, remove [freeStart, freeEnd] from each merged interval independently.
        """
        result = []

        for start, end in intervals:

            # No overlap
            if end < freeStart or start > freeEnd:
                result.append([start, end])
                continue

            # Left portion
            if start < freeStart:
                result.append([start, freeStart - 1])

            # Right portion
            if end > freeEnd:
                result.append([freeEnd + 1, end])

        return result

