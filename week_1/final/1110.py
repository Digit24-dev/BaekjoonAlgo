import sys

string = input()

cnt = 0
newNumber = string

while True:
    sum = 0
    cnt += 1

    # 각 자릿수 합
    for i in range(len(newNumber)):
        sum += int(newNumber[i])
    
    newNumber = newNumber[-1] + str(sum)[-1]

    # print(newNumber, string)

    if int(newNumber) == int(string):
        break


print(cnt)
    