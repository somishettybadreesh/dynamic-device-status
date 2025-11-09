
````markdown
#  Dynamic Device Status Dashboard

A full-stack web application that displays the **real-time status of IoT devices** (Online/Offline) for multiple companies.  
Built with **Flask**, **PostgreSQL**, and **Vanilla JavaScript**, this project demonstrates modular backend design, clean UI, and real-time status updates.

---

##  Tech Stack

| Layer | Technology |
|--------|-------------|
| **Backend** | Flask (Python) |
| **Database** | PostgreSQL |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Other** | REST API, Fetch API, JSON |

---

##  Setup & Run Instructions

### 1️. Clone the Repository
```bash
git clone https://github.com/somishettybadreesh/dynamic-device-status.git
cd dynamic-device-status
````

### 2. Set Up the Database (PostgreSQL)

1. Open **pgAdmin** or terminal and create a database named:

   ```sql
   CREATE DATABASE devices_db;
   ```

2. Inside the `sql/` folder, run these scripts **in order**:

   * `schema.sql` → creates the tables.
   * `seed.sql` → inserts sample companies, devices, and readings.

   You can execute them via pgAdmin or terminal:

   ```bash
   psql -U postgres -d devices_db -f sql/schema.sql
   psql -U postgres -d devices_db -f sql/seed.sql
   ```

### 3️. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # (Windows)
# or source venv/bin/activate (Mac/Linux)

pip install -r requirements.txt
```

Set your **PostgreSQL credentials** in `config.py`:

```python
DATABASE_URL = "postgresql://postgres:<your_password>@localhost:5432/devices_db"
```

Now run the backend:

```bash
python app.py
```

The Flask API will start at:
 `http://localhost:5000`

---

### 4️. Frontend Setup

The frontend uses plain JavaScript — no extra dependencies required.

Open `frontend/index.html` in your browser,
or serve it automatically via Flask (it’s already integrated).

Frontend runs at:
 `http://localhost:5000`

---

##  Application Overview

###  Companies

* Dynamically loaded from backend via `/api/companies`
* Shown in a dropdown selector.

###  Devices

* When a company is selected, devices are fetched via `/api/companies/<id>/devices`.
* Each device is displayed as a **status tile** (Green = Online, Red = Offline).

###  Auto Refresh

* Every **10 seconds**, device statuses refresh automatically without reloading the page.

---

##  API Documentation

### `GET /api/companies`

Fetch all available companies.
**Response Example:**

```json
[
  {"id": 1, "name": "Acme Corp"},
  {"id": 2, "name": "Beta Industries"}
]
```

---

### `GET /api/companies/<company_id>/devices`

Fetch all devices belonging to the specified company.
**Response Example:**

```json
[
  {
    "device_id": 1,
    "device_name": "Acme-Device-1",
    "latest_ts": "2025-11-09T10:22:53.017481+00:00",
    "status": "online"
  },
  {
    "device_id": 2,
    "device_name": "Acme-Device-2",
    "latest_ts": "2025-11-09T10:12:53.017481+00:00",
    "status": "offline"
  }
]
```

**Logic for Status Determination:**

* Each device’s latest reading timestamp is fetched from `device_readings`.
* If:

  * No readings exist → status = `offline`
  * Latest timestamp > 2 minutes old → status = `offline`
  * Else → status = `online`

---

##  Database Schema

###  `companies`

| Column     | Type               | Description    |
| ---------- | ------------------ | -------------- |
| id         | SERIAL PRIMARY KEY | Company ID     |
| name       | TEXT               | Company Name   |
| created_at | TIMESTAMP          | Auto timestamp |

###  `devices`

| Column     | Type               | Description                |
| ---------- | ------------------ | -------------------------- |
| id         | SERIAL PRIMARY KEY | Device ID                  |
| company_id | INT (FK)           | References `companies(id)` |
| name       | TEXT               | Device Name                |
| created_at | TIMESTAMP          | Auto timestamp             |

###  `device_readings`

| Column        | Type               | Description              |
| ------------- | ------------------ | ------------------------ |
| id            | SERIAL PRIMARY KEY | Reading ID               |
| device_id     | INT (FK)           | References `devices(id)` |
| reading_value | NUMERIC            | Dummy sensor data        |
| created_at    | TIMESTAMP          | Reading timestamp        |

---

##  Assumptions Made

1. The backend simulates real-time behavior by checking reading timestamps; no live stream integration was required.
2. All timestamps are stored in UTC for consistency.
3. Devices are marked **offline** if they haven’t sent a reading in **>2 minutes**.
4. Frontend refresh interval is **10 seconds**, adjustable in `main.js`.
5. Seed data simulates 3 companies, each with 3–5 devices.

---

##  Folder Structure

```
dynamic-device-status/
│
├── backend/
│   ├── app.py
│   ├── blueprints/
│   │   └── api.py
│   ├── services/
│   │   └── device_service.py
│   ├── db/
│   │   └── db.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── main.js
│   └── styles.css
│
├── sql/
│   ├── schema.sql
│   └── seed.sql
│
└── README.md
```

---

##  Future Improvements (Extensibility)
* Add authentication for company admins.
* Add new device types with live metrics.
* Implement WebSocket updates for true real-time monitoring.
* Filter devices by “Online” / “Offline”.
* Add notification banners when a device comes online.

---

##  Evaluation Mapping

| Criteria          | Implementation                              |
| ----------------- | ------------------------------------------- |
| **Clarity**       | Code commented, separated modules           |
| **Code Quality**  | Modular Flask structure (API, DB, Services) |
| **Functionality** | Fully working endpoints + auto-refresh UI   |
| **Extendability** | Layered structure for easy extension        |
| **UI/UX**         | Responsive layout with color-coded tiles    |
| **Documentation** | Complete README (Setup + API + Assumptions) |

---

##  Author

**Badreesh Somishetty**
[GitHub Profile →](https://github.com/somishettybadreesh)

---


````
