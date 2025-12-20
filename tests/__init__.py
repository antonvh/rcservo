"""Tests for the rcservo package"""

import pytest
from rcservo import scale


class TestScale:
    """Tests for the scale utility function"""

    def test_scale_basic(self):
        """Test basic scaling"""
        result = scale(50, (0, 100), (0, 1))
        assert result == 0.5

    def test_scale_negative_range(self):
        """Test scaling with negative ranges"""
        result = scale(0, (-90, 90), (1000, 2000))
        assert result == 1500

    def test_scale_inverted_ranges(self):
        """Test scaling with different range orders"""
        result = scale(75, (0, 100), (-1, 1))
        assert result == 0.5


if __name__ == "__main__":
    pytest.main([__file__])
