# System Architecture

## Status
🔲 Planned — Phase 2

## Component Overview
To be populated from Capella ARCADIA models.

## Interface Definitions
| Interface | Producer | Consumer | Data | Rate |
|---|---|---|---|---|
| IMU stream | Sensor model | EKF, TCN | accel(3) + gyro(3) | 100 Hz |
| GPS fix | Sensor model | EKF | pos(3) + vel(3) | 10 Hz |
| Camera frames | Sensor model | VO module | 640×480 RGB | 30 Hz |
| State estimate | EKF | Controller, TCN | pos+vel+att+bias | 100 Hz |
| Control command | Controller | Plant model | thrust + torques | 100 Hz |
| Fault flag | TCN | Mode manager | class + confidence | 10 Hz |
