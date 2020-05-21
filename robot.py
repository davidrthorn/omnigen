import math
import sys


def move(coordinates, heading):
    x, y = coordinates
    return [
        (x, y + 1),
        (x + 1, y),
        (x, y - 1),
        (x - 1, y),
    ][heading]  # readable, but not optimised. If/else would be faster if speed is a concern


# direction is 1 for clockwise, -1 for counter-clockwise
def rotate(heading, direction):
    return (heading + direction) % 4


def distance_between(coordinates_a, coordinates_b):
    a = abs(coordinates_a[0] - coordinates_b[0])
    b = abs(coordinates_a[1] - coordinates_b[1])

    return math.sqrt(a ** 2 + b ** 2)


def navigate(start_coordinates, start_heading, instructions):

    coordinates = start_coordinates
    heading = start_heading

    for instruction in instructions:
        if instruction == 'F':
            coordinates = move(coordinates, heading)
            yield coordinates

        elif instruction == 'R':
            heading = rotate(heading, 1)

        elif instruction == 'L':
            heading = rotate(heading, -1)

        else:
            raise Exception('unknown instruction: ', instruction)

    return coordinates


# file must have one instruction per line with no blank lines
def get_instructions(filename):
    with open(filename) as f:
        while True:
            instruction = f.readline().rstrip()
            if not instruction:
                return
            yield instruction


def parse_arguments(args):
    if len(args) < 5:
        raise ValueError("require 4 arguments: "
                         "[initial x coordinate] "
                         "[initial y coordinate] "
                         "[initial heading] "
                         "[instruction file name]")

    return (int(args[1]), int(args[2])), int(args[3]), args[4]


if __name__ == '__main__':

    supplied_coordinates, supplied_heading, supplied_instructions = parse_arguments(sys.argv)

    instruction_generator = get_instructions(supplied_instructions)

    generate_latest_coordinates = navigate(supplied_coordinates, supplied_heading, instruction_generator)

    ground_covered = 0  # just for fun
    for latest in generate_latest_coordinates:
        ground_covered = ground_covered + 1
        if latest == supplied_coordinates and ground_covered > 0:
            print("travelled in a circle and terminated journey")
            print("ground covered:     ", ground_covered)
            exit(0)

    print("final position:     ", latest)
    print("distance travelled: ", '%.3f' % distance_between(supplied_coordinates, latest))
    print("ground covered:     ", ground_covered)
