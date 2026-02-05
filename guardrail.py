# guardrail.py
import argparse
from common.config import load_config
from common.logging import setup_logging

def main():
    parser = argparse.ArgumentParser(
        description="Database Reliability & Security Guardrail"
    )
    parser.add_argument(
        "--config",
        required=True,
        help="Path to config.ini"
    )
    parser.add_argument(
        "--checks",
        default="all",
        help="Comma-separated list of checks to run"
    )
    parser.add_argument(
        "--output",
        default="./reports",
        help="Output directory"
    )

    args = parser.parse_args()

    config = load_config(args.config)
    logger = setup_logging()

    logger.info("Guardrail starting")
    logger.info(f"Checks requested: {args.checks}")

    # Placeholder for checks
    logger.info("No checks executed yet (skeleton mode)")

    logger.info("Guardrail complete")

if __name__ == "__main__":
    main()
