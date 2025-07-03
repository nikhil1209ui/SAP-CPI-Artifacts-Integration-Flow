# 🔍 Project Overview
This integration flow automates the process of retrieving customer order data via HTTP, saving it into a SQLite3 database, previewing the stored records, converting the data to CSV, and finally delivering the output to an SFTP server.

The end-to-end flow mimics a basic invoice generation process with real-world components and connectivity patterns.

# 📌 Integration Flow Steps
`Start`

 │
 
`[Request-Reply] (HTTP GET) — Get Orders (Flask API via Ngrok)`

 │
 
`[Request-Reply] (HTTP POST) — Save Orders in SQLite3 DB (Flask API via Ngrok)`

 │
 
`[Request-Reply] (HTTP GET) — Preview Stored Orders (Flask API via Ngrok)`

 │
 
`Groovy Script — Convert JSON Orders to CSV Format`

 │
 
`SFTP Receiver — Store Final CSV File on Remote Server (FileZilla)`

# 🧰 Technologies & Tools Used
- SAP Cloud Platform Integration (SAP CPI)

- Flask (Python) – For local APIs (order provider, order saver)

- Ngrok – Exposing Flask APIs to internet

- SQLite3 – Lightweight DB to store order records

- Groovy Script – For data transformation (JSON → CSV)

- FileZilla Server – For receiving CSV via SFTP

