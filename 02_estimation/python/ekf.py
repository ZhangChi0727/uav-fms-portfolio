"""
Extended Kalman Filter for UAV INS/GNSS fusion.

State vector (16-dim):
    position    [0:3]   — NED frame, metres
    velocity    [3:6]   — NED frame, m/s
    quaternion  [6:10]  — body-to-NED rotation
    accel_bias  [10:13] — accelerometer bias, m/s²
    gyro_bias   [13:16] — gyroscope bias, rad/s

Measurement sources:
    GPS:  position (NED) + velocity (NED)
    VO:   relative pose delta (position + attitude)

Reference:
    Titterton & Weston, "Strapdown Inertial Navigation Technology", 2nd ed.

Status: placeholder — Phase 3A
"""
from __future__ import annotations

import numpy as np


class EKF:
    """Extended Kalman Filter for INS/GNSS/VO fusion."""

    STATE_DIM = 16
    GPS_MEAS_DIM = 6   # position (3) + velocity (3)
    VO_MEAS_DIM = 6    # delta position (3) + delta attitude (3)

    def __init__(self) -> None:
        # State estimate
        self.x: np.ndarray = np.zeros(self.STATE_DIM)
        # Covariance matrix
        self.P: np.ndarray = np.eye(self.STATE_DIM)
        # Process noise covariance
        self.Q: np.ndarray = np.eye(self.STATE_DIM)
        # GPS measurement noise covariance
        self.R_gps: np.ndarray = np.eye(self.GPS_MEAS_DIM)
        # VO measurement noise covariance
        self.R_vo: np.ndarray = np.eye(self.VO_MEAS_DIM)

    def predict(self, accel: np.ndarray, gyro: np.ndarray, dt: float) -> None:
        """Propagate state and covariance using IMU measurements."""
        raise NotImplementedError("Phase 3A")

    def update_gps(self, z_gps: np.ndarray) -> None:
        """Correct state estimate using GPS position + velocity measurement."""
        raise NotImplementedError("Phase 3A")

    def update_vo(self, z_vo: np.ndarray) -> None:
        """Correct state estimate using Visual Odometry relative pose."""
        raise NotImplementedError("Phase 3A")

    def _compute_jacobian_F(
        self, accel: np.ndarray, gyro: np.ndarray, dt: float
    ) -> np.ndarray:
        """Compute state transition Jacobian F = df/dx."""
        raise NotImplementedError("Phase 3A")
