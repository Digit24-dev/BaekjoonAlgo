
def kmp_match(txt: str, pat: str) -> int:
    pt = 1          # txt를 따라가는 커서
    pp = 0          # pat을 따라가는 커서
    skip = [0] * (len(pat) + 1) # 건너뛰기 표
    
    # 건너뛰기 표 생성
    skip[pt] = 0
    while pt != len(pat):
        if pat[pp] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    
    # 문자열 검색
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1



if __name__ == '__main__':
    s1 = input()
    s2 = input()

    idx = kmp_match(s1, s2)

    if idx == -1:
        print("NO")
    else:
        print(f"{(idx + 1)} 번째 문자 일치")

