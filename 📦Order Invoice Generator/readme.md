# 🔍 Project Overview
This integration flow automates the process of retrieving customer order data via HTTP, saving it into a SQLite3 database, previewing the stored records, converting the data to CSV, and finally delivering the output to an SFTP server.

The end-to-end flow mimics a basic invoice generation process with real-world components and connectivity patterns.

# 📌 Integration Flow Steps

```scss
Start
 │
 ▼
[Request-Reply] (HTTP GET) — Get Orders (Flask API via Ngrok)
 │
 ▼
[Request-Reply] (HTTP POST) — Save Orders in SQLite3 DB (Flask API via Ngrok)
 │
 ▼
[Request-Reply] (HTTP GET) — Preview Stored Orders (Flask API via Ngrok)
 │
 ▼
Groovy Script — Convert JSON Orders to CSV Format
 │
 ▼
SFTP Receiver — Store Final CSV File on Remote Server (FileZilla)
```

# 🧰 Technologies & Tools Used
- SAP Cloud Platform Integration (SAP CPI)

- Flask (Python) – For local APIs (order provider, order saver)

- Ngrok – Exposing Flask APIs to internet

- SQLite3 – Lightweight DB to store order records

- Groovy Script – For data transformation (JSON → CSV)

- FileZilla Server – For receiving CSV via SFTP

# 🧠 Groovy Script Logic
```groovy
import com.sap.gateway.ip.core.customdev.util.Message
import groovy.json.JsonSlurper

def Message processData(Message message) {
    def body = message.getBody(String)
    def records = new JsonSlurper().parseText(body)

    def csv = new StringBuilder()
    csv.append("OrderID,Customer,Amount,Items,Country\n")

    records.each { row ->
        if (row instanceof List && row.size() >= 5) {
            def orderId = row[0]
            def customer = row[1]
            def amount = row[2]
            def items = row[3]
            def country = row[4]
            csv.append("${orderId},${customer},${amount},\"${items}\",${country}\n")
        }
    }

    message.setBody(csv.toString())
    return message
}

```
### ✅ Purpose: Converts JSON array of order records into a structured CSV format with proper handling for special characters (like commas in items).

# 🚀 How to Run This IFlow
1. Start Flask APIs locally on your machine:

   - /get_orders → Returns list of orders (GET)

   - /receive_orders → Saves order to SQLite3 DB (POST) and supports preview (GET)

2. Expose Flask endpoints using Ngrok and copy the public URLs into HTTP receiver channels.

3. Deploy the iFlow in your SAP CPI tenant.

4. Use Postman/FileZilla to verify:

   - Orders are fetched

   - Stored successfully

   - CSV is created and pushed to the remote server

## 📁 Sample Input
Example JSON payload fetched from /get_orders:
```json
[
  [101, "John Doe", 150.0, "Laptop,Mouse", "USA"],
  [102, "Jane Smith", 200.0, "Tablet", "Canada"]
]
```
## 📂 Output
CSV file stored in SFTP server:
```csv
OrderID,Customer,Amount,Items,Country
101,John Doe,150.0,"Laptop,Mouse",USA
102,Jane Smith,200.0,"Tablet",Canada
```
# 🙌 Credits
- Built by Nikhil Kushwaha
- Mock APIs and DB designed for internal learning purposes.
