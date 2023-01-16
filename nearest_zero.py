# ID 76074199

def nearest_zero(street_map, _zero='0'):
    street_size = len(street_map)
    output = [0] * street_size
    zeros = [
        index for index, value in enumerate(street_map) if value == _zero
    ]
    first_zero, last_zero = zeros[0], zeros[-1]
    for item in range(first_zero):
        output[item] = first_zero - item
    # output[:first_zero] = [first_zero - pos for pos in range(first_zero)]
    # при попытки переписать  все на  "векторизацию" увеличиваться время,
    # возможно не правильно переписал,но спасибо за полезную деталь.
    for item in range(len(zeros) - 1):
        zeros_item_1 = zeros[item + 1]
        for pos in range(zeros[item] + 1, zeros_item_1):
            output[pos] = min(
                pos - zeros[item],
                zeros_item_1 - pos
            )
    for item in range(last_zero + 1, street_size):
        output[item] = item - last_zero
    return output


if __name__ == '__main__':
    input()
    print(*nearest_zero(input().split()))
