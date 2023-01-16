# ID 79735620
def broken_search(nums, value) -> int:
    lower, upper, = 0, len(nums) - 1,
    while lower <= upper:
        left, right = nums[lower], nums[upper]
        if value == left:
            return lower
        if value == right:
            return upper
        medial = (lower + upper) // 2
        middle = nums[medial]
        if middle == value:
            return medial
        if left <= middle:
            if left < value < middle:
                upper = medial - 1
            else:
                lower = medial + 1
        else:
            if middle < value < right:
                lower = medial + 1
            else:
                upper = medial - 1
    return -1
