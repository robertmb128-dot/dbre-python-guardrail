BACKUP_QUERY = """
SELECT
    d.name AS database_name,
    MAX(b.backup_finish_date) AS last_backup_time,
    DATEDIFF(HOUR, MAX(b.backup_finish_date), GETDATE()) AS backup_age_hours
FROM sys.databases d
LEFT JOIN msdb.dbo.backupset b
    ON b.database_name = d.name
    AND b.type = 'D' -- Full backups only
WHERE d.state_desc = 'ONLINE'
GROUP BY d.name
ORDER BY d.name;
"""
