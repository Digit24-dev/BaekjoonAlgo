#####################################################
#                    풀이 1                         #
#####################################################
n=str(input())
m=n.split('-')
x=sum(map(int, (m[0].split('+'))))
ans=0

if n[0]=='-':
    ans-=x
else:
    ans+=x

for x in m[1:]:
    x=sum(map(int, (x.split('+'))))
    ans-=x
print(ans)

#####################################################
#                    풀이 2                         #
#####################################################

string = input().split('-')

result = 0

for i in string[0].split('+'):
    result += int(i)
for i in string[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)