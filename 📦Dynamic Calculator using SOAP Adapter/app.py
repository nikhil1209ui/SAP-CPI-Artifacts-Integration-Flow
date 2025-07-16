import streamlit as st
import requests
import xml.etree.ElementTree as et

cpi_url = "https://nikhil-s-trial-of96evfv.it-cpitrial03-rt.cfapps.ap21.hana.ondemand.com/http/calculate"

operations = {
    '➕': 'Add',
    '➖': 'Subtract',
    '✖️': 'Multiply',
    '➗': 'Divide'
}

st.title("SOAP Calculator")
int_A = st.number_input('Enter Integer A', step=1, format='%d')
int_B = st.number_input('Enter Integer B', step=1, format='%d')
op = st.radio('Select Operation', ["➕","➖","✖️","➗"])


if st.button('Calculate'):
    soap_operation = operations[op]

    xml_payload = f'''
     <ns0:{soap_operation} xmlns:ns0="http://tempuri.org/">
        <ns0:intA>{int_A}</ns0:intA>
        <ns0:intB>{int_B}</ns0:intB>
     </ns0:{soap_operation}>
     '''
    
    header = {'Content-Type': 'application/xml'}
    auth = ("sb-07735c9b-a4f2-41ca-bf06-efa31b89ee0b!b69137|it-rt-nikhil-s-trial-of96evfv!b196","0a0b6ed2-ba83-477e-a478-552a015b2726$x00QSdzgjXF0Tvwbwd28uLSY6C7fqHs8SpkceljVEYk=")
    response = requests.post(cpi_url, 
                             data=xml_payload.strip(), 
                             headers=header, 
                             auth=auth)

    if response.status_code == 200:  
        try:
            root = et.fromstring(response.content)
            result_tag = f"{{http://tempuri.org/}}{soap_operation}Result"
            result = root.find(f".//{result_tag}").text
            st.success(f"✅ Result: {result}")
        except:
            st.error("❌ Couldn't parse response!")
    else:
        st.error(f"❌ Failed with status code: {response.status_code}")

