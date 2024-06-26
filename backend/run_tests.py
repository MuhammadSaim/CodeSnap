import pytest
import sys
import os

def main():
    test_dir = "tests/"
    cov_dir = "htmlcov"

    # Ensure the test directory exists
    if not os.path.isdir(test_dir):
        print(f"Test directory '{test_dir}' does not exist.")
        sys.exit(1)

    # Pytest arguments
    pytest_args = [
        "--cov=application",  # Directory to measure coverage
        f"--cov-report=html:{cov_dir}",  # Coverage report in HTML format
        "--cov-report=term",  # Coverage report in terminal output
        test_dir  # Test directory
    ]

    # Run pytest with the specified arguments
    exit_code = pytest.main(pytest_args)

    # Exit with the same code pytest returned
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
