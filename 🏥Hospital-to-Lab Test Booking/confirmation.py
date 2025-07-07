from flask import Flask, request, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)
@app.route('/lab/bookings', methods=['POST'])

def handle_bookings():
    try:
        xml_data = request.data.decode("utf-8")
        root = ET.fromstring(xml_data)

        name = root.findtext('.//full_name')
        test = root.findtext('.//test_type')
        date = root.findtext('.//booking_date')

        print(f"Received booking for {name}'s {test} test on {date}")

        xml_status = f"""<lab_response>
        <status>Confirmed</status>
        </lab_response>"""

        return Response(xml_status, mimetype='application/xml', status=200)
    
    except Exception as e:
        error_msg = f"""<lab_response>
        <status>Failed</status>
        <error>{str(e)}</error>
        </lab_response>"""

        return Response(error_msg, mimetype='application/xml', status=500)
    
if __name__ == '__main__':
    app.run(port=5001)

# Optional: Save to SQLite
#        conn = sqlite3.connect('lab_bookings.db')
#        cursor = conn.cursor()
#        cursor.execute('''CREATE TABLE IF NOT EXISTS bookings 
#                          (name TEXT, test TEXT, date TEXT)''')
#        cursor.execute("INSERT INTO bookings VALUES (?, ?, ?)", (name, test, date))
#        conn.commit()
#        conn.close()

