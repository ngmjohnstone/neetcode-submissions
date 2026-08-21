class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        while len(rows) != numRows:
            if len(rows) == 0:
                rows.append([1])
            elif len(rows) == 1:
                rows.append([1, 1])
            else:
                lastRow = rows[-1]
                nextRow = [1]
                for i in range(len(lastRow) - 1):
                    nextRow.append(lastRow[i] + lastRow[i+1])
                nextRow.append(1)
                rows.append(nextRow)
        return rows