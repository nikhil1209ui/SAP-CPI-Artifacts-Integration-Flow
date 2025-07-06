# 🧠 Overview
Weather Report Generator is an SAP CPI Integration Flow that fetches current weather data using a public weather API based on a user-provided location and exports the result as a beautified CSV file to a remote SFTP server.

### This project demonstrates the use of:

- Dynamic input via HTTPS trigger

- Exchange Property manipulation via Content Modifier

- REST API consumption

- Data transformation using JSON-to-XML converter

- XML to CSV conversion using Groovy Script

- File delivery using SFTP Adapter

# 🚀 Flow Architecture
```scss
Sender (HTTPS / Postman trigger)
   |
   ▼
Start ▶ Content Modifier (sets API key and reads location from payload)
   |
   ▼
Request-Reply (HTTP Receiver - Calls Weather API)
   |
   ▼
JSON to XML Converter
   |
   ▼
Groovy Script (Beautifies and converts to CSV)
   |
   ▼
Receiver (SFTP - stores CSV on remote server)
```
## 📩 Input Payload
Sent via Postman or HTTPS trigger:
```json
desired location
```
(Just raw text — no JSON object, just a string representing the city.)

## 🔑 Content Modifier Configuration
Exchange Property 1:

`key`: Constant

Value: `"affafc027802424d88085920251706"`

Exchange Property 2:

`location`: Expression

Value: `${in.body}`

## 🌐 API Endpoint Used
```http
http://api.weatherapi.com/v1/current.json?key=${property.key}&q=${property.location}
```
Example Result Fields Used:

`region`, `country`, `localtime`, `temp_c`, `condition.text`

## 🧾 Output CSV Sample
```csv
Region,Country,Localtime,Temperature (C),Condition
Limpopo,South Africa,2025-07-03 15:09,24.9,Sunny
```
💻 Groovy Script (XML to CSV)
```groovy
import com.sap.gateway.ip.core.customdev.util.Message
import groovy.xml.XmlParser

def Message processData(Message message) {
    def body = message.getBody(String)
    def xml = new XmlParser().parseText(body)

    def region = xml.location.region.text()
    def country = xml.location.country.text()
    def localtime = xml.location.localtime.text()
    def temp_c = xml.current.temp_c.text()
    def condition = xml.current.condition.text.text()

    def csv = new StringBuilder()
    csv.append("Region,Country,Localtime,Temperature (C),Condition\n")
    csv.append("${region},${country},${localtime},${temp_c},${condition}\n")

    message.setBody(csv.toString())
    return message
}
```
## 📁 Receiver Configuration
Adapter Type: `SFTP`

Purpose: Stores `{date:now:yyyy-MM-dd}.csv` file in remote server for archiving/weather reporting, also helps generate date-specific reports on the remote SFTP server

Output: One CSV per trigger request.

## 📌 Key Concepts Demonstrated
- Dynamic input capture via Exchange Property

- External API call with runtime parameters

- Groovy scripting for custom CSV generation

- Cloud Integration to on-premise or cloud SFTP
## 📝 Ending Note
#### 🔁 Note on JSON-to-XML Converter:
  In the earlier version of this project, the JSON-to-XML converter was added because the output was needed in XML format for a different use case. Later, when the
  requirement changed to generate a CSV file via SFTP, I retained this component temporarily. However, a direct JSON-to-CSV conversion using Groovy is now the preferred and   optimized approach.

#### ⚙️ Automation Variant:
  I also created a second version of this iFlow which uses trigger automation to run the flow without manual input. It works best when you want daily reports for a fixed
  (constant) location.
