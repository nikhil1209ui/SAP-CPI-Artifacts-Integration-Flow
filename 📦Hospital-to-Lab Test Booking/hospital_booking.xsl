<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>

  <xsl:template match="/patient_record">
    <lab_booking>
      <patient>
        <full_name><xsl:value-of select="name"/></full_name>
        <test_type><xsl:value-of select="test"/></test_type>
        <booking_date><xsl:value-of select="date"/></booking_date>
        <email_address><xsl:value-of select="email"/></email_address>
      </patient>
    </lab_booking>
  </xsl:template>

</xsl:stylesheet>
