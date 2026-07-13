# Algorithm Failure Mode Analysis

## Status
🔲 Planned — Phase 5

## Failure Modes Under Analysis

### EKF
| Failure Mode | Cause | Effect | Mitigation |
|---|---|---|---|
| Filter divergence | Incorrect noise covariance | Unbounded position error | Covariance monitoring + reset |
| Jacobian singularity | Extreme attitude | NaN propagation | Quaternion normalization |

### Geometric Controller
| Failure Mode | Cause | Effect | Mitigation |
|---|---|---|---|
| Actuator saturation | Large tracking error | Loss of attitude control | Anti-windup, rate limiting |

### TCN Fault Detector
| Failure Mode | Cause | Effect | Mitigation |
|---|---|---|---|
| False positive | Sensor noise spike | Unnecessary mode switch | Threshold tuning, confirmation window |
| False negative | Novel fault signature | Undetected fault | Conservative threshold + time-out |
