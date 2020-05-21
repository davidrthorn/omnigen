# Robot navigation

To navigate the robot, run the script with `python robot.py [start x] [start y] [start heading] [instruction file name]`.

For example: `python robot.py 0 0 1 example.txt`

Instructions must be newline-separated lists of
letters, where 'F' is forward, 'R' is rotate clockwise 90deg,
'L' is rotate counter-clockwise 90deg (see included examples).
Instruction files must not include any blank lines between instructions.