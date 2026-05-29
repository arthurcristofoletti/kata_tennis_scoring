from src.app import Processor


def run_pipeline() -> str:
    """Orchestrates the pipeline execution flow."""
    processor = Processor(data_type="Ads Analytics")
    result = processor.process_element(500)
    print(f"[{processor.data_type}] Pipeline processing result: {result}")
    return f"Success: {result}"


if __name__ == "__main__":
    run_pipeline()
