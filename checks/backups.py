# checks/backups.py
from common.db import fetch_all
from common.logging import get_logger

logger = get_logger(__name__)

def run(config, reporter):
    logger.info("Running Backup Freshness / RPO check...")

    conn_string = config["database"]["connection_string"]
    rpo_hours = int(config["backups"]["rpo_hours"])

    results = fetch_all(conn_string, BACKUP_QUERY)

    for row in results:
        status = "OK"
        if row["backup_age_hours"] is None:
            status = "ALERT"
        elif row["backup_age_hours"] > rpo_hours:
            status = "ALERT"

        row["rpo_hours"] = rpo_hours
        row["status"] = status

        logger.info(
            "%s | last_backup=%s | age=%s | status=%s",
            row["database_name"],
            row["last_backup_time"],
            row["backup_age_hours"],
            status
        )

        reporter.add_result("backups", row)

    reporter.write("backups")
