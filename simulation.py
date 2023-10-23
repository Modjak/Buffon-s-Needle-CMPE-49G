import random
import math
import argparse

def buffon_simulation(N, L, D):
    if L >= D:
        raise ValueError("L must be less than D")

    count_crossings = 0

    for _ in range(N):
        # Step 1: Randomly generate the distance 'x' to the nearest line
        x = random.uniform(0, D / 2)

        # Step 2: Randomly generate the angle 'theta' between 0 and pi/2
        theta = random.uniform(0, math.pi / 2)

        # Step 3: Calculate the lower and upper bounds
        lower = x - (L / 2) * math.sin(theta)
        upper = x + (L / 2) * math.sin(theta)

        # Step 4: Check if the needle crosses a line
        if lower <= -D / 2 or upper >= D / 2:
            count_crossings += 1

    # Step 5: Calculate the estimated probability
    estimated_probability = count_crossings / N
    return estimated_probability


def main():
    parser = argparse.ArgumentParser(description='Monte Carlo Needle Simulation')
    parser.add_argument('N', type=int, help='Number of needles (N) to drop')
    parser.add_argument('L', type=float, help='Length of the needle (L)')
    parser.add_argument('D', type=float, help='Distance between lines (D)')

    args = parser.parse_args()

    estimated_prob = buffon_simulation(args.N, args.L, args.D)
    actual_prob = 2 * args.L / (math.pi * args.D)

    print("Estimated Probability: {:.5f}".format(estimated_prob))
    print("Actual Probability: {:.5f}".format(actual_prob))
    print('Accuracy: {:.2f}%'.format(100 * (1 - abs(actual_prob - estimated_prob) / actual_prob)))


if __name__ == "__main__":
    main()