class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row = ["" for _ in range(numRows)]

        curr_row = 0
        direction = 1 # 1 for going down and -1 for up

        for ch in s:
            row[curr_row] += ch

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1
            
            curr_row += direction
        
        print(row)
        return "".join(row)



# 2D approach
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s
#         mat = [['' for char in range(len(s))] for _ in range(numRows)]
#         row = 0
#         col = 0
#         going_down = True
#         for char in s:
#             mat[row][col] = char
#             # print(row, col, mat[row][col])

#             if going_down:
#                 if row == numRows - 1:
#                     going_down = False
#                     row-=1
#                     col+=1
#                 else:
#                     row+=1
#             else:
#                 if row==0:
#                     going_down=True
#                     row+=1
#                 else:
#                     row-=1
#                     col+=1
#         res = ""
#         for idx, row in enumerate(mat):
#             res+="".join(row)
#         # print(res)
#         return res


# [       0    1    2    3    4    5    6    7    8    9   10    11   12   13
#     0 ['P', ' ', 'A', ' ', 'H', ' ', 'N', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#     1 ['A', 'P', 'L', 'S', 'I', 'I', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#     2 ['Y', ' ', 'I', ' ', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# ]
# 0 0 P
# 1 0 A
# 2 0 Y
# 1 1 P
# 0 2 A
# 1 2 L
# 2 2 I
# 1 3 S
# 0 4 H-
# 1 4 I
# 2 4 R
# 1 5 I
# 0 6 N
# 1 6 G
# [
#     ['Y', 'P', 'I', 'S', 'R', 'I', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#     ['Y', 'P', 'I', 'S', 'R', 'I', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
#     ['Y', 'P', 'I', 'S', 'R', 'I', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# ]

