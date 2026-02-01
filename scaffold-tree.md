dbre-guardrail/
├── guardrail.py           # CLI entry point
├── README.md
│
├── checks/
│ ├── backups.py
│ ├── security.py
│ ├── config.py
│ └── jobs.py
│
├── common/
│ ├── db.py                 # Connection + query helpers
│ ├── logging.py            # Structured logging
│ ├── config.py             # Config loading
│ └── reporting.py          # Output generators
│
├── reports/
│ └── templates/
│
├── tests/
│ ├── test_backups.py
│ ├── test_security.py
│ └── test_config.py
│
├── sample_output/
│ ├── report.md
│ └── results.csv
└── requirements.txt
