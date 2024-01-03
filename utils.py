def find_max(arr: list) -> int:
    max = arr[0]
    for item in arr:
        if item>max:
            max=item
    return max

