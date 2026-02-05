# checks/backups.py
import datetime
import csv
from pathlib import Path
from common.logging import setup_logging

logger = setup_logging()

class BackupCheck:
    def __init__(self, db_connection, rpo_hours=24, output_dir="./reports"):
        self.db = db_connection
        self.rpo_hours = rpo_hours
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def get_last_backup_info(self):
        """
        Stub: Replace with real SQL query to fetch last backup datetime.
        Returns a list of dicts with 'database' and 'last_backup' keys.
        """
        # Example stub data
        return [
            {"database": "master", "last_backup": datetime.datetime.now() - datetime.timedelta(hours=20)},
            {"database": "sales", "last_backup": datetime.datetime.now() - datetime.timedelta(hours=30)},
        ]

    def run(self):
        logger.info("Running Backup Freshness / RPO check...")
        results = []
        now = datetime.datetime.now()

        for record in self.get_last_backup_info():
            db_name = record["database"]
            last_backup = record["last_backup"]
            age_hours = (now - last_backup).total_seconds() / 3600
            status = "OK" if age_hours <= self.rpo_hours else "ALERT"
            results.append({
                "database": db_name,
                "last_backup": last_backup.strftime("%Y-%m-%d %H:%M:%S"),
                "age_hours": round(age_hours, 2),
                "rpo_hours": self.rpo_hours,
                "status": status
            })
            logger.info(f"{db_name}: last backup {last_backup}, status: {status}")

        self.save_csv(results)
        self.save_markdown(results)
        return results

    def save_csv(self, results):
        csv_file = self.output_dir / "backup_check.csv"
        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        logger.info(f"CSV report saved to {csv_file}")

    def save_markdown(self, results):
        md_file = self.output_dir / "backup_check.md"
        with open(md_file, "w") as f:
            f.write("| Database | Last Backup | Age (hrs) | RPO (hrs) | Status |\n")
            f.write("|---------|------------|-----------|-----------|--------|\n")
            for r in results:
                f.write(f"| {r['database']} | {r['last_backup']} | {r['age_hours']} | {r['rpo_hours']} | {r['status']} |\n")
        logger.info(f"Markdown report saved to {md_file}")
