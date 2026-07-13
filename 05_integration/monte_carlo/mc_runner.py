"""
Monte Carlo runner: EKF vs UKF comparison.

Parameters swept:
    - GPS outage duration: [10, 30, 60, 120] seconds
    - Maneuver intensity: [hover, cruise, aggressive]
    - Noise seed: randomized per run

N = 500 runs per configuration.

Output: statistical tables + box plots saved to results/

Status: placeholder — Phase 4E
"""
