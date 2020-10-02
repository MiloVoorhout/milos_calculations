# Estimate pi, given you have random points between (0,1)
import random
import math


def estimate_pi(n):
    num_circle_points = 0
    num_total_points = 0

    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance_to_origin = math.sqrt(x ** 2 + y ** 2)

        if distance_to_origin <= 1:
            num_circle_points += 1
        num_total_points += 1

    return 4 * num_circle_points / num_total_points

