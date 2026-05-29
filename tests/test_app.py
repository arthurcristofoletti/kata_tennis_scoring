import pytest
from src.app import Processor


def test_processor_multiplication():
    """Validates the business logic transformation inside app.py."""
    processor = Processor(data_type="Test")
    assert processor.process_element(10) == 20


def test_processor_invalid_type():
    """Ensures the application raises a TypeError when receiving invalid data types."""
    with pytest.raises(TypeError):
        Processor(data_type=123)  # Should fail since it expects a string
