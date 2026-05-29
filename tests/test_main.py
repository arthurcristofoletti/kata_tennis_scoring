from src.main import run_pipeline


def test_main_pipeline_execution():
    """Validates that the main application entry point runs successfully."""
    assert run_pipeline() == "Success: 1000"
