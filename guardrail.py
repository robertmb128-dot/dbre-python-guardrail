from checks.backups import BackupCheck
from common.db import Database

# Initialize DB connection (stub for now)
db_conn = Database(config)
db_conn.connect()

# Determine which checks to run
checks_list = args.checks.split(",")
if "backups" in checks_list or "all" in checks_list:
    backup_check = BackupCheck(db_conn, rpo_hours=int(config.get("reliability", "rpo_hours", fallback=24)), output_dir=args.output)
    backup_check.run()

from checks.security import SecurityCheck
from checks.config import ConfigCheck

if "security" in checks_list or "all" in checks_list:
    security_check = SecurityCheck(db_conn, output_dir=args.output)
    security_check.run()

if "config" in checks_list or "all" in checks_list:
    config_check = ConfigCheck(db_conn, output_dir=args.output)
    config_check.run()

