# DBRE Python Guardrail

![Pre-release](https://img.shields.io/badge/release-v0.1--pre-orange?style=for-the-badge&logo=python&logoColor=white)
![GitHub Release](https://img.shields.io/github/v/release/robertmb128-dot/dbre-python-guardrail?label=latest%20release&style=for-the-badge)

**Python-based Database Reliability & Security Guardrail for SQL Server.**  
Encodes DBA and DBRE judgment into read-only, evidence-driven checks that validate backup reliability, configuration drift, and security posture.

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
