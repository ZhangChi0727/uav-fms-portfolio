"""
LQR attitude controller — linearized around hover equilibrium.

Used as baseline comparison against geometric controller.

Status: placeholder — Phase 3B
"""
from __future__ import annotations
import numpy as np


class LQRController:
    """Linear Quadratic Regulator for quadrotor attitude control."""

    def __init__(self) -> None:
        self.K: np.ndarray | None = None  # Gain matrix, computed offline

    def compute_gain(self, A: np.ndarray, B: np.ndarray,
                     Q: np.ndarray, R: np.ndarray) -> None:
        """Compute LQR gain matrix via scipy.linalg.solve_continuous_are."""
        raise NotImplementedError("Phase 3B")

    def compute_control(self, x_error: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Phase 3B")
