import unittest
import robot


class TestMove(unittest.TestCase):
    def test_performs_correct_transformation_for_heading(self):
        start = (0, 0)
        self.assertEqual(robot.move(start, 0), (0, 1))
        self.assertEqual(robot.move(start, 1), (1, 0))
        self.assertEqual(robot.move(start, 2), (0, -1))
        self.assertEqual(robot.move(start, 3), (-1, 0))

    def test_handles_negative_coordinates(self):
        start = (-12, 2)
        self.assertEqual(robot.move(start, 3), (-13, 2))


class TestRotate(unittest.TestCase):
    def test_returns_correct_value_for_clockwise(self):
        self.assertEqual(robot.rotate(0, 1), 1)
        self.assertEqual(robot.rotate(3, 1), 0)

    def test_returns_correct_value_for_counter_clockwise(self):
        self.assertEqual(robot.rotate(3, -1), 2)
        self.assertEqual(robot.rotate(0, -1), 3)


class TestDistanceBetween(unittest.TestCase):
    def test_works_for_positive_numbers(self):
        self.assertEqual(robot.distance_between((0, 0), (3, 4)), 5.0)

    def test_works_for_negative_numbers(self):
        self.assertEqual(robot.distance_between((0, 0), (-3, -4)), 5.0)

    def test_works_for_mixed_numbers(self):
        self.assertEqual(robot.distance_between((0, 0), (3, -4)), 5.0)

    def test_works_for_one_axis(self):
        self.assertEqual(robot.distance_between((0, 0), (0, -4)), 4.0)


class TestNavigate(unittest.TestCase):
    def test_yields_correct_latest_coordinates(self):
        instructions = ['F', 'R', 'F', 'L', 'F']
        expected = [(0, 1), (1, 1), (1, 2)]

        i = 0
        for c in robot.navigate((0, 0), 0, instructions):
            self.assertEqual(c, expected[i])
            i = i + 1

    def test_doesnt_move_without_forward_instructions(self):
        instructions = ['R', 'R', 'L', 'L']
        i = 0
        for _ in robot.navigate((0, 0), 0, instructions):
            i = i + 1

        self.assertEqual(i, 0)

    def test_raises_when_invalid_instruction(self):
        instructions = ['F', 'R', 'Q', 'L', 'F']

        self.assertRaises(Exception, robot.navigate((0, 0), 0, instructions))


if __name__ == '__main__':
    unittest.main()
