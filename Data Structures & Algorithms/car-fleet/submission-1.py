class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True) #按离target最近 -> 最远
        fleets = 0
        front_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > front_time:
                fleets += 1
                front_time = time
            
        return fleets


        