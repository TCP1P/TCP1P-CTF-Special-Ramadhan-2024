#!/bin/sh
set -eu
python3 - <<'PY'
import os
import sqlite3
from pathlib import Path
database = Path('/app/tcp1p.sqlite')
archived = bytes.fromhex('54435031507b6e3163335f316e6a3363745f623367316e5f313333377265707d').decode()
current = os.environ['RSCTF_FLAG']
connection = sqlite3.connect(database)
try:
    tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
    changed = 0
    for (table,) in tables:
        quoted_table = '"' + table.replace('"', '""') + '"'
        columns = connection.execute(f'PRAGMA table_info({quoted_table})').fetchall()
        for column in columns:
            name = column[1]
            quoted_column = '"' + name.replace('"', '""') + '"'
            cursor = connection.execute(
                f'UPDATE {quoted_table} SET {quoted_column}=replace({quoted_column}, ?, ?) WHERE typeof({quoted_column})=\'text\' AND instr({quoted_column}, ?) > 0',
                (archived, current, archived),
            )
            changed += cursor.rowcount
    if changed < 1:
        raise SystemExit('archived SQLite flag slot was not found')
    connection.commit()
finally:
    connection.close()
PY
