# checks/config.py
from pathlib import Path
import csv
from common.logging import setup_logging

logger = setup_logging()

class ConfigCheck:
    def __init__(self, db_connection, baseline_config=None, output_dir="./reports"):
        self.db = db_connection
        self.baseline_config = baseline_config or {
            "max_memory": 2147483648,
            "cost_threshold": 50
        }
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def get_current_config(self):
        """
        Stub: Replace with real SQL queries to fetch current server settings
        Returns dict of current settings per database
        """
        return {
            "master": {"max_memory": 2147483648, "cost_threshold": 50},
            "sales": {"max_memory": 1073741824, "cost_threshold": 75}  # Drift here
        }

    def run(self):
        logger.info("Running Configuration Drift Check...")
        current_config = self.get_current_config()
        results = []

        for db_name, settings in current_config.items():
            for key, baseline_value in self.baseline_config.items():
                current_value = settings.get(key)
                status = "OK" if current_value == baseline_value else "ALERT"
                results.append({
                    "database": db_name,
                    "setting": key,
                    "current_value": current_value,
                    "baseline_value": baseline_value,
                    "status": status
                })
                logger.info(f"{db_name} | {key} | {current_value} | {baseline_value} | {status}")

        if results:
            self.save_csv(results)
            self.save_markdown(results)

        return results

    def save_csv(self, results):
        csv_file = self.output_dir / "config_check.csv"
        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        logger.info(f"CSV report saved to {csv_file}")

    def save_markdown(self, results):
        md_file = self.output_dir / "config_check.md"
        with open(md_file, "w") as f:
            f.write("| Database | Setting | Current Value | Baseline Value | Status |\n")
            f.write("|---------|---------|---------------|----------------|--------|\n")
            for r in results:
                f.write(f"| {r['database']} | {r['setting']} | {r['current_value']} | {r['baseline_value']} | {r['status']} |\n")
        logger.info(f"Markdown report saved to {md_file}")
