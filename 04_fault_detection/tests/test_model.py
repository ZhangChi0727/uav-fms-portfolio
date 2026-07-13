"""
Unit tests for TCN model.

Status: test stubs — Phase 3C
"""
import torch
import pytest
from models.tcn import TCN


def test_output_shape() -> None:
    """TCN output shape must match (batch, n_classes)."""
    model = TCN()
    x = torch.randn(8, 6, 100)
    out = model(x)
    assert out.shape == (8, 6)


def test_no_nan_output() -> None:
    """Model must not produce NaN for random inputs."""
    pytest.skip("Phase 3C")
