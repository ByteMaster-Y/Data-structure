def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half) # 재귀 호출
        merge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <=  right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                    # a_list = [3, 3]
                    # right_ind += 1 → right_ind = 1
                    # alist_ind += 1 → alist_ind = 1
                left_ind += 1
            else:
                    # [6]의 남은 요소 6 추가.
                    # → a_list[1] = 6
                    # 병합 결과: [3, 6]
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
                # → a_list[0] = 3
            alist_ind += 1
        
# ----> 2, 3

        # 즉 left_ind = 0, alist_ind = 1
        while left_ind < len(left_half):
            # a_list = [3, 3]
            a_list[alist_ind] = left_half[left_ind]
            # 따라서 a_list = [3, 6]이 됨!
            left_ind += 1
            alist_ind += 1

        # left_half[left_ind] = 3
        # right_half[right_ind] = 2
        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1
            # [2, 9]가 된다
        # 즉 ([3, 6],[2, 9])
        # [3, 6, 2, 9]
        # --> 
        # [2, , , ,]