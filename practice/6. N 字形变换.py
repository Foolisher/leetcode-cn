class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        rows = [''] * numRows
        direction = -1
        for c in s:
            rows[i] += c
            if i == numRows -1 or i == 0:
                direction *= -1
            i += direction
        return ''.join(rows)

print(Solution().convert('PAYPALISHIRING', 3))

