n = "AYUSH"

s = n[::-1]
print(s)

# For Int
num = 146
temp = num
rev_no = 0

while temp > 0:
    digit = temp % 10               # 6 - 4 - 1
    rev_no = rev_no * 10 + digit    # 6 - 64 - 641
    temp = temp // 10               # 14 - 1 - 0
    print(temp)
