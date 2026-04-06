class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = ['u','r','d','l']
        dir_map = {
            'u' : (0,1),
            'd' : (0,-1),
            'l' : (-1,0), 
            'r' : (1,0)}

        curr_direction = 0
        max_distance = 0
        obstacles_set = set(tuple(obstacle) for obstacle in obstacles)
        position = [0,0]
        for command in commands:
            if command == -1:
                curr_direction = (curr_direction + 1) % 4
            elif command == -2:
                curr_direction = (curr_direction - 1) % 4
            else:
                for _ in range(command):
                    next_pos = (position[0] + dir_map[directions[curr_direction]][0], position[1] + dir_map[directions[curr_direction]][1])
                    if next_pos not in obstacles_set:
                        position = next_pos
                    else:
                        break
                    max_distance = max(max_distance, position[0]**2 + position[1]**2)
        return max_distance


