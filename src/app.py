class Processor:
    """Responsible for handling core data transformation logic."""

    def __init__(self, data_type: str) -> None:
        if not isinstance(data_type, str):
            raise TypeError("Data type must be a string")
        self.data_type: str = data_type.strip()

    def process_element(self, value: int) -> int:
        """Executes a simple mathematical transformation on a numeric value."""
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        return int(value * 2)
