# ID 76066242

def max_point(finger, matrix, players=2, digits='123456789'):
    return sum(0 < matrix.count(time) <= finger * players
               for time in digits)


if __name__ == "__main__":
    print(max_point(
        int(input()),
        f'{input()}{input()}{input()}{input()}'
        )
    )
