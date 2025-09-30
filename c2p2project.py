"""
Pigeonhole Principle - Sock Selection Problem
Complete Implementation for Discrete Mathematics Project

Author: [Student Name]
Date: September 2024
Course: Discrete Mathematics
"""

import random
import math
from collections import Counter

def pigeonhole_socks_simulation(num_trials=10000, verbose=False):
    """
    Simulates the sock selection process to demonstrate the Pigeonhole Principle

    Args:
        num_trials (int): Number of simulation trials to run
        verbose (bool): Whether to print detailed trial information

    Returns:
        tuple: (success_rate, results_list, detailed_stats)
    """
    # Represent 10 pairs of socks (20 socks total) with different colors
    socks = []
    for color in range(10):  # 10 different colors (0-9)
        socks.extend([color, color])  # 2 socks of each color

    results = []
    pair_counts = []
    color_distributions = []

    for trial in range(num_trials):
        # Shuffle the socks to randomize selection
        random.shuffle(socks)

        # Pick 11 socks randomly
        selected_socks = socks[:11]

        # Count frequency of each color
        color_count = Counter(selected_socks)

        # Check if we have at least one matching pair
        has_matching_pair = any(count >= 2 for count in color_count.values())
        results.append(has_matching_pair)

        # Count total number of pairs
        num_pairs = sum(1 for count in color_count.values() if count >= 2)
        pair_counts.append(num_pairs)

        # Store color distribution for analysis
        color_distributions.append(dict(color_count))

        # Display first few trials if verbose
        if verbose and trial < 5:
            print(f"Trial {trial + 1}:")
            print(f"  Selected socks (by color): {selected_socks}")
            print(f"  Color frequency: {dict(color_count)}")
            print(f"  Has matching pair: {has_matching_pair}")
            print(f"  Number of pairs: {num_pairs}")
            print("-" * 50)

    # Calculate statistics
    success_rate = sum(results) / len(results)
    avg_pairs = sum(pair_counts) / len(pair_counts)
    max_pairs = max(pair_counts)
    min_pairs = min(pair_counts)

    detailed_stats = {
        'success_rate': success_rate,
        'average_pairs': avg_pairs,
        'max_pairs': max_pairs,
        'min_pairs': min_pairs,
        'pair_distribution': Counter(pair_counts)
    }

    return success_rate, results, detailed_stats

def mathematical_analysis():
    """
    Provides detailed mathematical analysis of the Pigeonhole Principle application
    """
    print("Mathematical Analysis - Pigeonhole Principle Application")
    print("=" * 60)

    # Problem parameters
    total_socks = 20
    colors = 10
    socks_per_color = 2
    selected = 11

    print("\n1. Problem Setup:")
    print(f"   • Total socks: {total_socks}")
    print(f"   • Number of colors: {colors}")
    print(f"   • Socks per color: {socks_per_color}")
    print(f"   • Socks selected: {selected}")

    print("\n2. Pigeonhole Principle Application:")
    print(f"   • Pigeons (selected socks): {selected}")
    print(f"   • Pigeonholes (colors): {colors}")
    print(f"   • Since {selected} > {colors}, guarantee exists")

    # Combinatorial analysis
    total_ways = math.comb(total_socks, selected)
    ways_no_pairs = 0  # Impossible to select 11 socks with no matching pairs

    print("\n3. Combinatorial Analysis:")
    print(f"   • Total ways to select {selected} from {total_socks}: {total_ways:,}")
    print(f"   • Ways to select with NO pairs: {ways_no_pairs}")
    print(f"   • Probability of at least one pair: {1.0:.6f} (100%)")

    # Minimum guarantee calculation
    min_for_guarantee = colors + 1
    print("\n4. General Formula:")
    print(f"   • Minimum socks for guarantee: {min_for_guarantee}")
    print(f"   • Formula: min_socks = num_colors + 1")

    return {
        'total_ways': total_ways,
        'probability': 1.0,
        'min_guarantee': min_for_guarantee
    }

def generalized_analysis():
    """
    Extended analysis for different scenarios and generalizations
    """
    print("\nGeneralized Pigeonhole Analysis")
    print("=" * 50)

    def min_socks_for_pair(num_colors):
        """Calculate minimum socks needed to guarantee a matching pair"""
        return num_colors + 1

    # Test different scenarios
    scenarios = [
        (5, 2, 10),   # 5 colors, 2 per color, 10 total
        (10, 2, 20),  # 10 colors, 2 per color, 20 total (our case)
        (15, 2, 30),  # 15 colors, 2 per color, 30 total
        (20, 3, 60),  # 20 colors, 3 per color, 60 total
    ]

    print("\nScenario Analysis:")
    print("Colors | Per Color | Total | Min for Guarantee | Status")
    print("-" * 55)

    for colors, per_color, total_socks in scenarios:
        min_needed = min_socks_for_pair(colors)
        status = "✓ Possible" if min_needed <= total_socks else "✗ Impossible"
        print(f"{colors:6} | {per_color:9} | {total_socks:5} | {min_needed:17} | {status}")

    return scenarios

def probability_distribution_analysis(simulation_results):
    """
    Analyzes the distribution of matching pairs from simulation

    Args:
        simulation_results: Results from pigeonhole_socks_simulation
    """
    success_rate, results, detailed_stats = simulation_results

    print("\nProbability Distribution Analysis")
    print("=" * 45)

    print(f"Success Rate: {success_rate:.4f} ({success_rate*100:.2f}%)")
    print(f"Average pairs per trial: {detailed_stats['average_pairs']:.2f}")
    print(f"Range of pairs: {detailed_stats['min_pairs']} - {detailed_stats['max_pairs']}")

    print("\nDistribution of pair counts:")
    for pairs, frequency in sorted(detailed_stats['pair_distribution'].items()):
        percentage = (frequency / len(results)) * 100
        print(f"  {pairs} pairs: {frequency:5} trials ({percentage:5.2f}%)")

def main():
    """
    Main function to run all analyses
    """
    print("PIGEONHOLE PRINCIPLE - SOCK SELECTION PROBLEM")
    print("=" * 80)

    # Run mathematical analysis
    math_results = mathematical_analysis()

    # Run generalized analysis
    generalized_analysis()

    # Run simulation
    print("\n" + "=" * 80)
    print("SIMULATION RESULTS")
    print("=" * 80)

    simulation_results = pigeonhole_socks_simulation(num_trials=10000, verbose=True)

    # Analyze probability distribution
    probability_distribution_analysis(simulation_results)

    print("\n" + "=" * 80)
    print("CONCLUSION")
    print("=" * 80)
    print("The Pigeonhole Principle guarantees that selecting 11 socks")
    print("from 10 pairs of different colored socks will ALWAYS result")
    print("in at least one matching pair. This is mathematically certain")
    print("with a probability of 100%.")

if __name__ == "__main__":
    main()
