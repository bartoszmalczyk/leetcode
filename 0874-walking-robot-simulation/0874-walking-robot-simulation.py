class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_direction = 0
        max_distance = 0
        obstacles_set = set(tuple(obstacle) for obstacle in obstacles)
        position = [0,0]
        for command in commands:
            temp = 0
            if command == -1: temp = 1
            elif command == -2: temp = -1
            else:
                for _ in range(command):
                    dx, dy = directions[curr_direction]
                    next_pos = (position[0] + dx, position[1] + dy)
                    if next_pos not in obstacles_set:
                        position = next_pos
                    else:
                        break
                max_distance = max(max_distance, position[0]**2 + position[1]**2)
            curr_direction = (curr_direction + temp) % 4
        return max_distance


