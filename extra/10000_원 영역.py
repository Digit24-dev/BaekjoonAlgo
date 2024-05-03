import sys
n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    # '왼쪽 점인지 오른쪽 점인지 여부'와 '점의 위치'를 저장한다.
    circles.append(("L", x - r)) # 왼쪽 점 = 중심 - 반지름
    circles.append(("R", x + r)) # 오른쪽 점 = 중심 + 반지름

# 오른쪽 점 R이 왼쪽 점 L보다 앞으로 오도록 정렬 (왼쪽 점과 오른쪽 점이 만나는 경우, 닫히는 점인 오른쪽이 먼저 있어야 함)
circles.sort(key=lambda x: (x[0]),  reverse=True)
# 왼쪽 점부터 오름차순으로 정렬
circles.sort(key=lambda x: x[1])

for i in circles:
    print(i)

stack = [] # 왼쪽 점과 완성된 원의 정보를 담을 스택
count = 1 # 영역 개수

for circle in circles:
    # 현재 점이 왼쪽 점인 경우들만, stack에 담아둔다.
    if circle[0] == "L":
        stack.append(circle)
        continue

    # 현재 점이 '오른쪽 점'인 경우에만 아래 코드 수행

    # 현재 열린 원 안에 원이 들어있을 경우, 그 원들의 너비를 전부 더해서 담을 변수
    # -> 이게 현재 원의 크기와 같으면 현재 원을 꽉 채우고 있으므로 count를 2 증가시켜줄 예정
    total_width = 0

    while stack:
        # 스택에 가장 최근에 쌓인 것 꺼냄
        prev = stack.pop()

        # L을 꺼낸 경우 == 스택에서 꺼낸 게 왼쪽 점인 경우 -> 원이 만들어짐
        if prev[0] == "L":

            # 너비 = 현재 점(오른쪽 점) - 이전 점(왼쪽 점)
            width = circle[1] - prev[1]

            # 현재 만들어진 원의 지름이 이전의 원들 지름의 합과 같을 경우
            # 현재 원을 꽉 채우고 있으므로 count를 2 증가
            if total_width == width:
                count += 2
                # 다를 경우, count 1 증가
            else:
                count += 1

            # 원이 만들어졌으므로 stack에 원을 의미하는 C와 너비 추가
            stack.append(("C", width))

            # 원이 닫히면 다음으로 넘어간다.
            # 지금 원을 추가했기 때문에 stack에 값이 있어서 break를 안해주면 탈출하지 못한다!!
            break

        # C를 꺼낸 경우 == 스택에서 꺼낸 게 원인 경우 -> 현재 원 안에 존재하는 원을 의미
        elif prev[0] == "C":
            total_width += prev[1]

print(count)