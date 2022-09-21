def check_input(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if isinstance(arr[i][j], int):
                continue;
            else:
                return False
    # colomns and rows check respectivly
    for i in range(n):
        for j in range(n):
            temp = arr[j][i]
            for k in range(n):
                if temp == arr[k][i] and k != j:
                    return False
                else:
                    continue

    for i in range(n):
        for j in range(n):
            temp = arr[i][j]
            for k in range(n):
                if temp == arr[i][k] & k != j:
                    return False
                else:
                    return True