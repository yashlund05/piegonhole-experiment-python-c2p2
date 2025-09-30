Pigeonhole Principle: Sock Selection Problem
Project Overview
This project demonstrates the Pigeonhole Principle through the classic sock selection problem, offering both rigorous mathematical proof and Python simulation.

Problem Statement
Given a drawer containing 10 pairs of socks in different colors (total 20 socks), if 11 socks are picked randomly, prove that at least one pair will match in color using the Pigeonhole Principle.

Solution Approach
Mathematical Proof:
The Pigeonhole Principle states that if more items (socks picked) than containers (colors) are distributed, at least one container must contain more than one item.
In this case, picking 11 socks from 10 color categories guarantees at least one matching color pair.

Combinatorial Analysis:
It is impossible to pick 11 socks without any matching color, as there are only 10 distinct colors.

Python Simulation:
The code simulates picking 11 socks from 20, verifying that every trial results in at least one matching pair. Detailed statistical results are generated for validation.

Usage Instructions
Clone the repository and ensure the Python environment is set up.

Run the main Python file (pigeonhole_socks_complete.py) to observe simulation output in the console.

The simulation displays sample draws, color frequencies, and overall success rate.

Review the included project report for theoretical proof and further analysis.

Example to run:

bash
python pigeonhole_socks_complete.py
Results Interpretation
Success rate: 100% in all simulation runs

Average pairs found per trial: Approximately 2.2

Minimum guaranteed matching pairs per draw: 1

Files Included
pigeonhole_socks_complete.py: Full Python implementation

pigeonhole-sock-report.md: Detailed academic report with proofs, results, and generalizations

Credits
Project by YASH LUND
Discrete Mathematics coursework, 2024-2025
Vishwakarma University, Pune

