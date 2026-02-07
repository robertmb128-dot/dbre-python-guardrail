# DBRE Python Guardrail

![Pre-release](https://img.shields.io/badge/release-v0.1--pre-orange?style=for-the-badge&logo=python&logoColor=white)
![GitHub Release](https://img.shields.io/github/v/release/robertmb128-dot/dbre-python-guardrail?label=latest%20release&style=for-the-badge)

**Python-based Database Reliability & Security Guardrail for SQL Server**  
Encodes DBA and DBRE judgment into read-only, evidence-driven checks that validate **backup reliability, configuration drift, and security posture**.

---

## Overview

DBRE Python Guardrail is designed to help SQL Server teams **surface operational risks early**, **reduce manual audits**, and **provide defensible evidence for compliance**.  
This pre-release includes the CLI skeleton and the first three checks, all producing **audit-ready console, CSV, and Markdown outputs**.

**Checks included in v0.1-pre:**
- **Backup Freshness / RPO Check** – verifies last backup timestamp against defined RPO
- **Security Check** – detects orphaned users and excessive privileges
- **Configuration Drift Check** – identifies deviations from baseline server settings

---

## Quick CLI Usage

```bash
python guardrail.py --config config.ini --checks all --output ./reports
