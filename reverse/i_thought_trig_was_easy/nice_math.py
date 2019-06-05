import math

def nice_math(x, y):
    return round(x + y*math.cos(math.pi * x))

lots_of_nums = lambda n,a:(lambda r:[*r,n-sum(r)])(range(n//a-a//2,n//a+a//2+a%2))

def get_number(char):
    return ord(char) - 96

inp = input("Enter the text: ")

out = []
for i in range(0, len(inp)):
    for j in lots_of_nums(nice_math(get_number(inp[i]), len(inp) - i), i + 1):
        out.append(nice_math(j, i + 1))
print(out)
