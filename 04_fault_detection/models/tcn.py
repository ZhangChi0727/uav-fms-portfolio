"""
Temporal Convolutional Network (TCN) for sensor fault classification.

Architecture:
    Input:  (batch, channels=6, window=100) — accel (3) + gyro (3)
    Stack:  N residual TCN blocks with dilated causal convolutions
    Output: (batch, n_classes=6) — fault type logits

Reference:
    Bai et al., "An Empirical Evaluation of Generic Convolutional and
    Recurrent Networks for Sequence Modeling", 2018.

Status: placeholder — Phase 3C
"""
from __future__ import annotations
import torch
import torch.nn as nn


class TemporalBlock(nn.Module):
    """Single residual TCN block with dilated causal convolution."""

    def __init__(self, in_channels: int, out_channels: int,
                 kernel_size: int, dilation: int) -> None:
        super().__init__()
        padding = (kernel_size - 1) * dilation
        self.conv1 = nn.Conv1d(in_channels, out_channels, kernel_size,
                               padding=padding, dilation=dilation)
        self.conv2 = nn.Conv1d(out_channels, out_channels, kernel_size,
                               padding=padding, dilation=dilation)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.chomp = lambda x: x[:, :, :-padding]
        self.residual = (nn.Conv1d(in_channels, out_channels, 1)
                         if in_channels != out_channels else nn.Identity())

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("Phase 3C")


class TCN(nn.Module):
    """Full TCN for multivariate time-series fault classification."""

    def __init__(self, in_channels: int = 6, n_classes: int = 6,
                 n_filters: int = 64, n_layers: int = 6,
                 kernel_size: int = 3) -> None:
        super().__init__()
        # Phase 3C: build layer stack with exponential dilation

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("Phase 3C")
