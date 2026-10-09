class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_num, last_den = 0, 1        # last fleet's time as a fraction

        for pos, spd in cars:
            num = target - pos           # numerator of this car's time
            den = spd                    # denominator

            # Compare num/den > last_num/last_den  ⇔  num*last_den > last_num*den
            if num * last_den > last_num * den:
                fleets += 1
                last_num, last_den = num, den

        return fleets