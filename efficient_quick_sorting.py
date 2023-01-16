# ID 79758896

def quicksort(array):
    def sort(low, high):
        if low >= high:
            return -1
        left, right = low, high
        pivot = array[low]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while pivot < array[right]:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left, right = left + 1, right - 1
        sort(low=low, high=right)
        sort(low=left, high=high)

    sort(0, len(array) - 1)
    return array


if __name__ == '__main__':
    print(
        *[username for (_, _, username) in quicksort(
            list(
                (lambda username, solved, errors:
                 (-int(solved), int(errors), username))
                (*input().split())
                for _ in range(int(input()))
            )
        )], sep='\n'
    )
