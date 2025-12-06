# slope_to_intercept = {
        #     [slope]: {
        #         [intercepts]: []
        #     }
        # }

        # y1 = ax1 + b
        # -> a = (y1 - b) / x1
        # y2 = ax2 + b 
        # y2 = (y1 - b) * x2 / x1 + b
        # x1 y2 = y1 * x2 - b * x2 + bx1
        # x1 * y2 - y1 * x2 = (x1 -x2) * b
        # b = (x1 * y2 - y1 * x2) / (x1 - x2)
 
        # -> slope = y1 - y2 / x1 - x2
        # -> intercept = 
# class Solution:

    
        
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points) -> int:
        n = len(points)
        inf = 10**12  # just a big number to represent "infinite slope"

        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                # ----- compute slope k -----
                if x1 == x2: 
                    k = inf  # vertical
                    b = x1   # x-intercept (vertical line)
                else:
                    k = (y2 - y1) / (x2 - x1)

                    # Your intercept formula:
                    # b = (x1*y2 - y1*x2) / (x1 - x2)
                    b = (x1 * y2 - y1 * x2) / (x1 - x2)

                # ----- midpoint (doubled) -----
                mid = (x1 + x2) * 10000 + (y1 + y2)

                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        ans = 0
        print(slope_to_intercept)
        print(mid_to_slope)
        # -----------------------------------------
        # Count trapezoids
        # -----------------------------------------
        for intercept_list in slope_to_intercept.values():
            if len(intercept_list) < 2:
                continue

            freq = defaultdict(int)
            for b_val in intercept_list:
                freq[b_val] += 1

            total_sum = 0
            for count in freq.values():
                ans += total_sum * count
                total_sum += count

        # -----------------------------------------
        # Count parallelograms
        # -----------------------------------------
        for slope_list in mid_to_slope.values():
            if len(slope_list) < 2:
                continue

            freq = defaultdict(int)
            for k_val in slope_list:
                freq[k_val] += 1

            total_sum = 0
            for count in freq.values():
                ans -= total_sum * count
                total_sum += count

        return ans


points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
sol = Solution()
sol.countTrapezoids(points)