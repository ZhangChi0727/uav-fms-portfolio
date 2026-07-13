# 02 — State Estimation

## Contents
- `python/` — EKF and UKF implementations in Python
- `cpp/` — EKF reimplemented in C++17 with pybind11 Python bindings
- `benchmarks/` — Python vs C++ runtime comparison

## Algorithm: Extended Kalman Filter (EKF)
State vector: [position (3), velocity (3), attitude quaternion (4), IMU biases (6)]
Measurement sources: GPS position + velocity, Monocular VO relative pose

## Status
🔲 Planned — Phase 3A (Python), Phase 3D (C++)
