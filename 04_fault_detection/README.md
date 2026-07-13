# 04 — Fault Detection

## Contents
- `pipeline/` — Data preprocessing and PyTorch Dataset
- `models/` — TCN architecture and ablation variants
- `train.py` — Training script with W&B logging
- `evaluate.py` — Confusion matrix, ROC curve, detection latency

## Fault Types Detected
| Label | Description |
|---|---|
| 0 | Nominal (no fault) |
| 1 | Accelerometer bias |
| 2 | Gyroscope drift |
| 3 | Sensor noise spike |
| 4 | GPS position dropout |
| 5 | GPS position spoof |

## Status
🔲 Planned — Phase 3C
