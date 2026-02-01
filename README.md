# Database Reliability & Security Guardrail (Python)

## Overview
**Python-based Database Reliability & Security Guardrail for SQL Server.** This project encodes DBA and DBRE judgment into read-only, evidence-driven checks that validate **backup reliability, configuration drift, and security posture**. It is designed for SQL Server environments to help surface operational and security risks early, reduce manual audits, and provide defensible evidence for compliance.

---

## What This Tool Answers
> *Is this database environment safe, compliant, and reliable right now?*

It does so by running deterministic checks and producing audit-ready outputs.

---

## Design Principles
- **Read-only by default** – safety first
- **Idempotent checks** – safe to run repeatedly
- **Evidence-driven** – outputs can be handed to auditors or leadership
- **Operator-grade** – clear logs, exit codes, and failure semantics
- **Composable** – each check stands alone, but fits a system

---

## Initial Scope (v1)

### Reliability Checks
- Backup freshness vs defined RPO
- Backup history trend analysis
- Restore viability (logical validation)
- SQL Agent job failure detection

### Security Checks
- Orphaned user detection
- Excessive privilege identification (sysadmin, db_owner)
- Encryption state verification (TDE)

### Configuration Guardrails
- Configuration drift detection (approved baseline)
- High-risk setting identification

---

## Outputs
- Console summary (operator-friendly)
- CSV (data analysis)
- JSON (machine-readable)
- Markdown report (audit / evidence-ready)

---

## Repository Structure
```
dbre-guardrail/
├── guardrail.py              # CLI entry point
├── README.md
│
├── checks/
│   ├── backups.py
│   ├── security.py
│   ├── config.py
│   └── jobs.py
│
├── common/
│   ├── db.py                 # Connection + query helpers
│   ├── logging.py            # Structured logging
│   ├── config.py             # Config loading
│   └── reporting.py          # Output generators
│
├── reports/
│   └── templates/
│
├── tests/
│   ├── test_backups.py
│   ├── test_security.py
│   └── test_config.py
│
├── sample_output/
│   ├── report.md
│   └── results.csv
└── requirements.txt
```

---

## Configuration
Configuration is externalized to support multiple environments.

Example:
```ini
[database]
server = sql-prod-01
port = 1433
database = master
auth = windows

[reliability]
rpo_hours = 24

[output]
format = markdown,csv,json
```

---

## Usage (Planned)
```bash
python guardrail.py \
  --config config.ini \
  --checks backups,security,config \
  --output ./reports
```

Exit codes are meaningful and suitable for CI/CD integration.

---

## Why This Exists
Modern database environments fail quietly until they fail loudly. This project exists to surface **risk early**, **prove posture continuously**, and **reduce reliance on tribal knowledge**.

This is Database Reliability Engineering applied pragmatically.

---

## Roadmap
- [ ] CLI skeleton
- [ ] Backup freshness check (v1 anchor)
- [ ] Orphaned user detection
- [ ] Privilege risk scoring
- [ ] Markdown report generator
- [ ] CI/CD example integration

---

## Author Intent
This repository is built as a **professional artifact**, not a tutorial. Every check reflects real-world DBA and DBRE concerns encountered in production SQL Server environments.

