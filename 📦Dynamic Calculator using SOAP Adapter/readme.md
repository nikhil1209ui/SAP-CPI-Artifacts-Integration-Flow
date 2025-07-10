## 🧮 SAP CPI Project: Dynamic Calculator using SOAP Adapter
A real-time iFlow that dynamically handles basic arithmetic operations—Addition, Subtraction, Multiplication, and Division—based on user payload input and 
routes to the appropriate SOAP operation using the [DNE Online Calculator API](http://www.dneonline.com/calculator.asmx?WSDL).

## 📌 Overview
This integration flow demonstrates dynamic routing in SAP CPI based on the SOAP operation received in the request payload (Add, Subtract, Multiply, or Divide). The flow extracts operands and operation type using a Content Modifier, and routes the request to the corresponding SOAP endpoint using a router and message mapping.

## 🧠 Architecture
```mathematica
[HTTPS Sender]
     |
[Content Modifier] → Extracts operation, intA, intB
     |
   [Router]
     |--------- If operation = Add        → [Mapping] → [SOAP ReqReply] → [Receiver1]
     |--------- If operation = Subtract   → [Mapping] → [SOAP ReqReply] → [Receiver2]
     |--------- If operation = Multiply   → [Mapping] → [SOAP ReqReply] → [Receiver3]
     |--------- If operation = Divide     → [Mapping] → [SOAP ReqReply] → [Receiver4]
     |
     |--------- Else → End (Invalid Input)
```
## 🧰 Technologies and Components Used
- SAP Cloud Integration (CPI)

- HTTPS Sender Adapter

- SOAP Receiver Adapter

- Content Modifier

- Router

- Message Mapping

- Request–Reply Pattern

- DNE Online SOAP Calculator API

## 📩 Sample Input Payload (Postman)
```xml
<ns0:Add xmlns:ns0="http://tempuri.org/">
    <ns0:intA>20000</ns0:intA>
    <ns0:intB>99999</ns0:intB>
</ns0:Add>
```
#### ⚠️ The root tag changes depending on the operation:

```<ns0:Add>, <ns0:Subtract>, <ns0:Multiply>, <ns0:Divide>```

## 📤 Output (SOAP Response)
```xml
<AddResponse xmlns="http://tempuri.org/">
  <AddResult>119999</AddResult>
</AddResponse>
```
Similarly:

SubtractResponse

MultiplyResponse

DivideResponse

## 🧾 Content Modifier – XPath Extraction
- Used to extract operation and operands:

   - Operation:
     ```xpath
        local-name(/*)
     ```
   - intA
    ```xpath
      /*/*[local-name()='intA']
    ```
   - intB:
    ```xpath
      /*/*[local-name()='intB']
    ```
These are stored as properties like operation, intA, and intB.

## 🔁 Routing Logic
Router condition (Expression Type: XPath):
```xpath
local-name(/*) = 'Add'      → Route(+)
local-name(/*) = 'Subtract' → Route(-)
local-name(/*) = 'Multiply' → Route(*)
local-name(/*) = 'Divide'   → Route(/)
Default (null or no match): End the flow gracefully.
```

## 🧩 Message Mapping
Each operation has a dedicated Message Mapping step that maps the incoming dynamic structure to the exact SOAP request structure expected by the DNE Calculator API.

## ⚙️ SOAP Receiver Configuration
Set manually for each operation (since WSDL only binds to one operation at a time):
- Field	Value
  - Address:	http://www.dneonline.com/calculator.asmx
  - URL to WSDL:	http://www.dneonline.com/calculator.asmx?WSDL
  - Service:	Calculator
  - Endpoint:	CalculatorSoap
  - Operation Name:	Add / Subtract / Multiply / Divide (per receiver)
  - Authentication:	None

✅ Don’t forget to press Select after entering the WSDL to populate fields.

## 💬 Response Handling
Each branch ends with the SOAP Response being returned back to the sender via HTTPS.

## 🧠 Future Improvements
🔄 Single Dynamic SOAP Receiver: Build raw SOAP envelopes in Groovy for all 4 operations and use 1 HTTP receiver.


## 👨‍💻 Credits
Project Designed and Developed by
🧑‍💻 Nikhil Kushwaha
Aspiring SAP CPI Consultant & Integration Developer
