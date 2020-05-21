import math

def move(coordinates, heading):
    x, y = coordinates
    return [
        (x, y + 1),
        (x + 1, y),
        (x, y - 1),
        (x - 1, y),
    ][heading]


# direction is 1 for clockwise, -1 for counter-clockwise
def rotate(heading, direction):
    return (heading + direction) % 4


def handle_unknown(instruction):
    raise Exception('unknown instruction: ', instruction)


def distance_between(coordinates_a, coordinates_b):
    a = abs(coordinates_a[0] - coordinates_b[0])
    b = abs(coordinates_a[1] - coordinates_b[1])
    return math.sqrt(a ** 2 - b ** 2)


test_instructions = [
    'R', 'F', 'L', 'F'
]


def navigate(start_coordinates, start_heading, instructions=[]):
    start_coordinates = (0, 0)
    start_heading = 0  # North=0, East=1, South=2, West=3

    coordinates = start_coordinates  # will this mutate?
    heading = start_heading

    for instruction in test_instructions:
        if instruction == 'F':
            coordinates = move(coordinates, heading)
        if instruction in ['R', 'L']:
            direction = 1 if instruction == 'R' else -1
            heading = rotate(heading, direction)
        else:
            handle_unknown(instruction)

    return coordinates


if __name__ == '__main__':
    navigate((0, 0), 1, test_instructions)