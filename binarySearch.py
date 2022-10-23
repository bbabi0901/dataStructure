# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.


def binary_search(L, x):
    lower = 0
    upper = len(L) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if x < L[middle]:
            upper = middle - 1
        elif x > L[middle]:
            lower = middle + 1
        else:
            return middle
    return -1


def recursive_binary_search(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return recursive_binary_search(L, x, l, mid-1)
    else:
        return recursive_binary_search(L, x, mid+1, u)



# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0