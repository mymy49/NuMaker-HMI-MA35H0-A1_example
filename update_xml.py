import re

xml_file = "/home/mymy49/git-repository/examples/NuMaker-HMI-MA35H0-A1_example/example/MA35H0_Registers.xml"

timer_xml = """
    <!-- TIMER0 : 타이머 0 -->
    <RegisterGroup description="Timer Controller 0" name="TIMER0" start="0x40500000">
        <Register access="Read/Write" description="Timer Control Register" name="CTL" reset_mask="0xFFFFFFFF" reset_value="0x00000005" size="4" start="+0x0000"/>
        <Register access="Read/Write" description="Timer Comparator Register" name="CMP" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0004"/>
        <Register access="Read/Write" description="Timer Interrupt Status Register" name="INTSTS" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0008"/>
        <Register access="Read/Write" description="Timer Data Register" name="CNT" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x000C"/>
        <Register access="ReadOnly" description="Timer Capture Data Register" name="CAP" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0010"/>
        <Register access="Read/Write" description="Timer External Control Register" name="EXTCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0014"/>
        <Register access="Read/Write" description="Timer External Interrupt Status Register" name="EINTSTS" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0018"/>
        <Register access="Read/Write" description="Timer Trigger Control Register" name="TRGCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x001C"/>
        <Register access="Read/Write" description="Timer Alternative Control Register" name="ALTCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0020"/>
    </RegisterGroup>

    <!-- TIMER1 : 타이머 1 -->
    <RegisterGroup description="Timer Controller 1" name="TIMER1" start="0x40500100">
        <Register access="Read/Write" description="Timer Control Register" name="CTL" reset_mask="0xFFFFFFFF" reset_value="0x00000005" size="4" start="+0x0000"/>
        <Register access="Read/Write" description="Timer Comparator Register" name="CMP" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0004"/>
        <Register access="Read/Write" description="Timer Interrupt Status Register" name="INTSTS" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0008"/>
        <Register access="Read/Write" description="Timer Data Register" name="CNT" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x000C"/>
        <Register access="ReadOnly" description="Timer Capture Data Register" name="CAP" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0010"/>
        <Register access="Read/Write" description="Timer External Control Register" name="EXTCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0014"/>
        <Register access="Read/Write" description="Timer External Interrupt Status Register" name="EINTSTS" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0018"/>
        <Register access="Read/Write" description="Timer Trigger Control Register" name="TRGCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x001C"/>
        <Register access="Read/Write" description="Timer Alternative Control Register" name="ALTCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0020"/>
    </RegisterGroup>
"""

with open(xml_file, "r") as f:
    content = f.read()

if "TIMER0" not in content:
    new_content = content.replace("</Processor>", timer_xml + "</Processor>")
    with open(xml_file, "w") as f:
        f.write(new_content)
    print("Added TIMER0 and TIMER1 to XML.")
else:
    print("TIMER0 already in XML.")
