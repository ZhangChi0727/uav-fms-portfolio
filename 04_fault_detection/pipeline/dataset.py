"""
PyTorch Dataset for IMU fault detection.

Status: placeholder — Phase 3C
"""
from __future__ import annotations
import torch
from torch.utils.data import Dataset


class FaultDataset(Dataset):
    """Sliding window dataset over multivariate IMU sensor streams."""

    def __init__(self, path: str, window_size: int = 100, stride: int = 10) -> None:
        self.window_size = window_size
        self.stride = stride
        # TODO Phase 3C: load HDF5, build index

    def __len__(self) -> int:
        raise NotImplementedError("Phase 3C")

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        raise NotImplementedError("Phase 3C")
