## 🔄 Overview
- This integration flow processes .xml files received via SFTP, validates them, and then routes the data to two parallel channels:

- One transforms the XML to JSON and forwards it to a designated folder.

- The other transforms the XML to CSV and delivers it to another folder.

- If any error occurs during transformation or routing, the message is forwarded to an error folder using an Exception Subprocess.

## 🔗 Integration Flow Design
```php
Sender (SFTP)
   ↓
XML Validator
   ↓
Router (Multicast - Parallel Processing)
 ├── XML → JSON Converter → Receiver (SFTP: json_receiver)
 └── XML → CSV Converter → Receiver (SFTP: csv_receiver)
       ↓
  Exception Subprocess:
     Error Start → End → Receiver (SFTP: error folder)
```
## ⚙️ Flow Details
- Sender Adapter:
  - Protocol: SFTP
  - Purpose: Listens for incoming .xml files from a specific folder.

- XML Validator:
  - Validates the incoming XML against a predefined XSD schema.
  - If validation fails, the message is routed to the Exception Subprocess.

- Router (Multicast):
  - Type: Parallel Multicast
  - Purpose: Sends the message to two branches simultaneously.

## 📤 Branch 1: XML to JSON Conversion
- Adapter: XML to JSON Converter

- Receiver: SFTP (Folder: json_receiver)

- Use Case: Downstream systems that require structured JSON.

## 📤 Branch 2: XML to CSV Conversion
- Adapter: XML to CSV Converter

- Receiver: SFTP (Folder: csv_receiver)

- Use Case: Teams needing flat-file (CSV) reports for analytics or BI tools.

## ⚠️ Exception Subprocess
- Trigger: Any error in the flow (especially validation or conversion failures).
- Steps:
  - Error Start
  - End (no transformation inside — only redirection)
  - Receiver: SFTP (Folder: error folder)

- Use Case: Maintain visibility into failed payloads for debugging and correction.

## ✅ Key Features
- Supports parallel data transformation (JSON & CSV).

- Ensures data quality via XSD validation.

- Graceful error handling with auto-routing to an error folder.
