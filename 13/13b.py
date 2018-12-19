from pprint import pprint


tracks = list(map(list, open('13.txt').read().split('\n')))
# tracks = list(map(list, open('13-example2.txt').read().split('\n')))

carts = []
for row_idx, row in enumerate(tracks):
    for col_idx, direction in enumerate(row):
        if direction in ('>', '<', '^', 'v'):
            carts.append([row_idx, col_idx, direction, 0])
            # replace carts with track
            if direction in ('>', '<'):
                tracks[row_idx][col_idx] = '-'
            else:
                tracks[row_idx][col_idx] = '|'

carts = list(sorted(carts, key=lambda pos: pos[0]))  # sort by rows

def print_tracks():
    global tracks, carts
    cart_idx = 0

    for row_idx, row in enumerate(tracks):
        for col_idx, direction in enumerate(row):
            cart = carts[cart_idx] if cart_idx < len(carts) else [-1, -1]
            if cart[0] == row_idx and cart[1] == col_idx:
                print(cart[2], end='')

                cart_idx += 1
            else:
                print(direction, end='')
        print()


dir_to_dr_dc = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

next_direction = {
    '>': {'\\': 'v', '/': '^', '-': '>'},
    '<': {'\\': '^', '/': 'v', '-': '<'},
    '^': {'\\': '<', '/': '>', '|': '^'},
    'v': {'\\': '>', '/': '<', '|': 'v'}
}

next_direction_plus = {
    '>': {0: '^', 1: '>', 2: 'v'},
    '<': {0: 'v', 1: '<', 2: '^'},
    '^': {0: '<', 1: '^', 2: '>'},
    'v': {0: '>', 1: 'v', 2: '<'}
}

def tick():
    global tracks, carts
    collided = set()
    for cart_idx, [row_idx, col_idx, direction, state] in enumerate(carts):
        # make movement
        dr, dc = dir_to_dr_dc[direction]
        new_row_idx, new_col_idx = row_idx + dr, col_idx + dc
        new_state = state
        # change direction
        new_state = state
        if tracks[new_row_idx][new_col_idx] == '+':  # intersection
            new_direction = next_direction_plus[direction][state]
            new_state = (new_state + 1) % 3
        else:  # no intersection
            new_direction = next_direction[direction][tracks[new_row_idx][new_col_idx]]

        carts[cart_idx] = [new_row_idx, new_col_idx, new_direction, new_state]

        # check for colliding into another cart
        for cart2_idx in range(cart_idx+1, len(carts)):
            cart2 = carts[cart2_idx]
            if cart2[0] == new_row_idx and cart2[1] == new_col_idx:
                collided.add(cart_idx)
                collided.add(cart2_idx)
    carts = list(sorted(carts, key=lambda pos: pos[0] * 1000 + pos[1]))  # sort by rows

    for i in range(len(carts)-1):
        for j in range(i+1, len(carts)):
            cart_i = carts[i]
            cart_j = carts[j]
            if cart_i[0] == cart_j[0] and cart_i[1] == cart_j[1]:
                collided.add(i)
                collided.add(j)

    new_carts = []
    for i in range(len(carts)):
        if i not in collided:
            new_carts.append(carts[i])

    carts = new_carts

    # print_tracks()

    if len(carts) == 1:
        print(carts[0][1], carts[0][0])
        return True

    return False

while True:
    if tick():
        break
