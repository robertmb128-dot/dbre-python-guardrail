### Backup Freshness / RPO Check

**Purpose:**  
Ensures each SQL Server database meets its defined Recovery Point Objective (RPO) by verifying the age of the last backup. This check is **read-only**, audit-ready, and designed to provide evidence for reliability and compliance.

**Location:**  
`checks/backups.py`

---

#### How it Works
1. Retrieves the last backup timestamp for each database (stubbed or via SQL query).  
2. Compares backup age against the defined RPO threshold.  
3. Assigns a status of **OK** or **ALERT** for each database.  
4. Generates outputs:
   - **CSV** (`reports/backup_check.csv`)  
   - **Markdown** (`reports/backup_check.md`)  
   - Structured logs (console)

---

#### CLI Usage

```bash
python guardrail.py --config config.ini --checks backups --output ./reports
