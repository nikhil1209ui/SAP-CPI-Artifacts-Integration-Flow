## 🏥 Hospital-to-Lab Test Booking
This SAP CPI Integration Flow simulates a real-world hospital booking system that connects with a diagnostic lab system. 
It automates test booking, handles success/failure scenarios, and sends personalized email notifications based on response status.

### 📘 Overview
- Goal: Enable a hospital system to book lab tests through an external lab API.
- Highlights: Real-time patient booking, XSLT-based XML transformation, dynamic email notifications for both success and failure, with robust exception handling.
- Trigger: HTTPS (Postman request)
- Response: Lab booking confirmation or failure notice

### 🔧 Flow Overview
```scss
HTTPS Sender (Postman)
   ↓
Content Modifier (Extract: name, test, date, email)
   ↓
XSLT Mapping (Convert patient XML to lab-compatible XML)
   ↓
Request-Reply → HTTP Receiver (Flask Lab API → returns <status>)
   ↓
Router:
   ├── If <status> = Confirmed → Mail Receiver (Send success email)
   └── Else (Default Route) → Exception Subprocess
                             → Mail Receiver (Send failure alert)
```
### 🧰 Technologies & Components Used
| Component            | Purpose                                   |
| -------------------- | ----------------------------------------- |
| Postman              | API Testing Tool                          |
| Flask (Python)       | Simulated Lab System API                  |
| XSLT                 | Transform hospital XML to lab format      |
| Groovy Script        | To trigger exception handling |
| Content Modifier     | Extract fields from XML                   |
| Router               | Check `<status>` and branch flow          |
| Exception Subprocess | Handle failures with alert email          |
| Mail Adapter         | Send confirmation/failure email           |

### 📨Sample Payload (XML Input from Postman)
```xml
<patient_record>
  <name>patient name</name>
  <test>test type</test>
  <date>##-##-####</date>
  <email>name@example.com</email>
</patient_record>
```
### 📦Expected Output Payload (Lab Response)
```xml
<lab_response>
  <status>Confirmed</status>
</lab_response>
```
### 📨 Email Notifications
#### ✅ Success Email:
```bash
🎉 Lab Booking Confirmed

Dear Patient name,

Your test has been successfully booked for ##-##-####.

Thank you for choosing our hospital.

– Hospital Admin
```
#### ❌ Failure Email (from Exception Subprocess):
```bash
❗ Lab Booking Failed

Dear Patient name,

We regret to inform you that your test scheduled for ##-##-#### could not be booked due to a system issue.

Please contact support for assistance.

– Hospital Admin
```
### 🔁 XSLT Code Snippet (Transformation for this particular case): [.xsl file](https://github.com/nikhil1209ui/SAP-CPI-Artifacts-Integration-Flow/blob/main/%F0%9F%8F%A5Hospital-to-Lab%20Test%20Booking/confirmation.py)
----
### 🔧 Mail Adapter Configuration
| Field          | Value                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------- |
| From           | Gmail (for testing)                                                                      |
| To             | `${property.email}`                                                                      |
| Authentication | Use Secure Parameters (Gmail SMTP or configured mail server)                             |
| Subject        | Lab response                                                                             |
| Body           | Uses exchange properties like `${property.name}`, `${property.date}`, `${property.test}` |
#### ✅ CPI fetches these properties from initial Content Modifier.

#### 🧪 Groovy Script
Used to trigger exception
```groovy
import com.sap.gateway.ip.core.customdev.util.Message

def Message processData(Message message) {
    throw new Exception("Lab booking failed: status not confirmed")
}
```

### 🧩 Flask App Overview (Lab API): [.py file](https://github.com/nikhil1209ui/SAP-CPI-Artifacts-Integration-Flow/blob/main/%F0%9F%8F%A5Hospital-to-Lab%20Test%20Booking/confirmation.py)

#### 🧪 Testing Tools
- Postman: Send test payloads to iFlow
- Simulation: Used for intermediate CPI debugging
- Gmail SMTP: Send confirmation/failure emails
- Flask + Ngrok: Mock lab API exposed to internet

#### 📌 Key Concepts Demonstrated
- iFlow orchestration with branching logic
- Real-time API communication
- Dynamic property extraction
- XSLT transformation
- Exception subprocess + error routing
- Conditional email handling

### 🔄 Future Enhancement: SQLite DB Integration
- In the upcoming version of this project, we plan to persist patient booking records into a local SQLite3 database for audit or reporting purposes.
#### 🗂️The Flask app [.py](https://github.com/nikhil1209ui/SAP-CPI-Artifacts-Integration-Flow/blob/main/%F0%9F%8F%A5Hospital-to-Lab%20Test%20Booking/confirmation.py) already contains the necessary code to save booking data into the database — it’s currently commented for this version but included in the repository for easy reactivation.

#### This would allow extended features like:
- Booking history tracking
- Duplicate booking checks
- Offline storage for lab system backups

### 🙌 Credits
- Developed and maintained by Nikhil Kushwaha
- Portfolio-ready project demonstrating real-world integration

