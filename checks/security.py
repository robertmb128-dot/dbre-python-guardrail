# checks/security.py
from pathlib import Path
import csv
from common.logging import setup_logging

logger = setup_logging()

class SecurityCheck:
    def __init__(self, db_connection, output_dir="./reports"):
        self.db = db_connection
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def get_security_risks(self):
        """
        Stub: Replace with real SQL queries to detect:
        - Orphaned users
        - Excessive privileges (sysadmin, db_owner)
        Returns list of dicts with 'database', 'user', 'risk_type', 'severity'
        """
        return [
            {"database": "master", "user": "orphan_user1", "risk_type": "orphaned", "severity": "HIGH"},
            {"database": "sales", "user": "db_owner_user", "risk_type": "excess_privilege", "severity": "MEDIUM"}
        ]

    def run(self):
        logger.info("Running Security Check...")
        results = self.get_security_risks()

        for r in results:
            logger.info(f"{r['database']} | {r['user']} | {r['risk_type']} | {r['severity']}")

        if results:
            self.save_csv(results)
            self.save_markdown(results)
        else:
            logger.info("No security risks detected")

        return results

    def save_csv(self, results):
        csv_file = self.output_dir / "security_check.csv"
        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        logger.info(f"CSV report saved to {csv_file}")

    def save_markdown(self, results):
        md_file = self.output_dir / "security_check.md"
        with open(md_file, "w") as f:
            f.write("| Database | User | Risk Type | Severity |\n")
            f.write("|---------|------|----------|---------|\n")
            for r in results:
                f.write(f"| {r['database']} | {r['user']} | {r['risk_type']} | {r['severity']} |\n")
        logger.info(f"Markdown report saved to {md_file}")
