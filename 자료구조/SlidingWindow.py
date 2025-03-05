def max_sum_subarray(arr, k):
    # 배열의 길이와 구간의 크기를 확인
    n = len(arr)
    if n < k:
        return "구간 크기가 배열보다 큽니다."
    
    # 첫 번째 구간의 합을 계산 (arr[0]부터 arr[k-1]까지의 합)
    window_sum = sum(arr[:k])  # 첫 번째 3개의 요소의 합: 2 + 1 + 5 = 8
    print(window_sum)
    max_sum = window_sum  # 첫 번째 구간의 합을 초기 최대합으로 설정
    
    # 슬라이딩 윈도우 시작
    for i in range(n - k):  # n - k = 6 - 3 = 3 -> 3번 반복 (i는 0, 1, 2)
        # 현재 구간 합에서 arr[i]를 빼고 arr[i + k]를 더한다.
        # 첫 번째 이동: window_sum = 8 - arr[0] + arr[3] = 8 - 2 + 1 = 7
        # 두 번째 이동: window_sum = 7 - arr[1] + arr[4] = 7 - 1 + 3 = 9
        # 세 번째 이동: window_sum = 9 - arr[2] + arr[5] = 9 - 5 + 2 = 6
        window_sum = window_sum - arr[i] + arr[i + k]
        # 갱신된 window_sum과 max_sum 중 더 큰 값을 max_sum에 저장
        max_sum = max(max_sum, window_sum)  # max(8, 7, 9, 6) -> 9
    
    return max_sum

# 배열과 구간 크기
arr = [2, 1, 5, 1, 3, 2]
k = 3  # 구간 크기

# 결과 출력
print(f"크기가 {k}인 연속된 구간의 최대합: {max_sum_subarray(arr, k)}")
