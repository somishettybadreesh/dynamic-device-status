from db.db import query
from datetime import datetime, timezone, timedelta
import config

GET_COMPANIES_SQL = "SELECT id, name FROM companies ORDER BY id;"

GET_DEVICES_WITH_LATEST_SQL = """
SELECT d.id AS device_id,
       d.name AS device_name,
       lr.latest_ts
FROM devices d
LEFT JOIN (
  SELECT device_id, MAX(created_at) AS latest_ts
  FROM device_readings
  GROUP BY device_id
) lr ON d.id = lr.device_id
WHERE d.company_id = %s
ORDER BY d.id;
"""

def get_companies():
    return query(GET_COMPANIES_SQL) or []

def get_devices_with_status(company_id):
    rows = query(GET_DEVICES_WITH_LATEST_SQL, (company_id,)) or []
    threshold = timedelta(seconds=config.ONLINE_THRESHOLD_SECONDS)
    now = datetime.now(timezone.utc)
    devices = []

    for r in rows:
        latest_ts = r.get("latest_ts")
        status = "offline"  # default
        latest_iso = None

        if latest_ts:
            if latest_ts.tzinfo is None:
                latest_ts = latest_ts.replace(tzinfo=timezone.utc)
            latest_iso = latest_ts.isoformat()
            diff = now - latest_ts

            if diff <= threshold:
                status = "online"

        devices.append({
            "device_id": r["device_id"],
            "device_name": r["device_name"],
            "latest_ts": latest_iso,
            "status": status
        })

    print(f"[DEBUG] Company {company_id}: Device statuses -> {devices}")
    return devices
