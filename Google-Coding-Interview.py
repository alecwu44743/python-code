import random

def estimate_pi(n):
    circle_point = 0
    total_point = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            circle_point += 1
        total_point += 1

    return 4 * circle_point / total_point
