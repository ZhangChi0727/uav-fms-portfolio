# Algorithm Performance Requirements

## Status
🔲 Planned — Phase 1

## Navigation Requirements
| ID | Description | Threshold | Verification |
|---|---|---|---|
| NAV-REQ-001 | Position error during 30s GPS outage (95th pct) | < 5m | Test + Analysis |
| NAV-REQ-002 | EKF update cycle time | < 10ms | Analysis |

## Control Requirements
| ID | Description | Threshold | Verification |
|---|---|---|---|
| CTL-REQ-001 | Attitude settling time — 10° step input | < 0.8s | Test |
| CTL-REQ-002 | Attitude overshoot | < 15% | Test |
| CTL-REQ-003 | Cross-track error at cruise | < 1.2m | Test |

## Fault Detection Requirements
| ID | Description | Threshold | Verification |
|---|---|---|---|
| FDI-REQ-001 | IMU bias fault detection latency | < 2s | Test |
| FDI-REQ-002 | False alarm rate (clean data, 100s) | < 1% | Test + Analysis |
| FDI-REQ-003 | GPS spoof detection latency | < 3s | Test |
