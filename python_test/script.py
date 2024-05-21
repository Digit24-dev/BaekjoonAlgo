import matplotlib.pyplot as plt
import random

# 초기값 설정
a = 0    # load_avg
b = 1    # threads
c = 0    # decay
d = 0    # recent_cpu
nice = 1
priority = 63

a_values = [a]  # a의 값들을 저장할 리스트
b_values = [b]  # b의 값들을 저장할 리스트
c_values = [c]  
d_values = [d]  # recent_cpu
f_values = [priority]

# 수식에 따른 a값 업데이트 및 랜덤한 b값 업데이트
for i in range(500):  # 100번의 스텝을 가정
    # b = random.uniform(1, 10)  # b를 0에서 2 사이의 랜덤한 값으로 업데이트
    b += 1

    # b = 1
    d += 1            # every clock tick, recent_cpu += 1

    if i % 4 == 0:
        priority = 63 - (d / 4) - (nice * 2)

    if i % 100 == 0:
        a = 59/60 * a + b/60
        d = d * c + nice
        c = (2 * a) / (2 * a + 1)

    a_values.append(a)
    b_values.append(b)
    c_values.append(c)
    d_values.append(d)
    f_values.append(priority)

# 그래프 그리기
plt.plot(a_values, label='load_avg')  # a 값에 대한 그래프
plt.plot(b_values, label='rdy_thr', linestyle='--')  # b 값에 대한 그래프, 점선으로 표시
plt.plot(c_values, label='decay')
plt.plot(d_values, label='recent_cpu')
plt.plot(f_values, label='priority')
plt.title('Change of a and b over time with random b')
plt.xlabel('Time step')
plt.ylabel('Value of a and b')
plt.grid(True)
plt.legend()  # 범례 표시
plt.show()
