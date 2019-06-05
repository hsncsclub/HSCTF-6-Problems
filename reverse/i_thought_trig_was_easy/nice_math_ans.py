import math

def solve_eq(ans, y):
    if (ans + y) % 2 == 0:
        return ans - y
    else:
        return ans + y

def get_letter(num):
    return chr(num + 96)

inp = [-25, 1, 10, 7, 4, 7, 2, 9, 3, 8, 1, 10, 3, -1, -8, 3, -6, 5, -4, 7, -5, 8, -3, 10, -1, 12, 10, 7, -6, 9, -4, 11, -2, 13, -2, -11, 6, -9, 8, -7, 10, -5, 12, 1, -12, 7, -10, 9, -8, 11, -6, 13, -4, 11, 6, -13, 8, -11, 10, -9, 12, -7, 14, -5, 22, -16, 7, -14, 9, -12, 11, -10, 13, -8, 15, -6, -2, 2, -21, 4, -19, 6, -17, 8, -15, 10, -13, 12, -11, 5]
char = 0
total = math.floor(math.sqrt(2*(len(inp) + 1))) - 1
print(total)
i = 0
num_array = []
while i < len(inp):
    char += 1
    add_num = 0
    for j in range(0, char + 1):
        add_num += solve_eq(inp[i], char)
        i += 1
    num_array.append(solve_eq(add_num, total - char + 1))

ans_array = []
for num in num_array:
    ans_array.append(get_letter(num))
print(ans_array)        
