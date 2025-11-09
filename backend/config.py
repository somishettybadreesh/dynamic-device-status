import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:moon2003@localhost:5432/devices_db")

# Device considered online if latest reading <= 120 seconds
ONLINE_THRESHOLD_SECONDS = int(os.getenv("ONLINE_THRESHOLD_SECONDS", "120"))
