import os

xml_file = "/home/mymy49/git-repository/examples/NuMaker-HMI-MA35H0-A1_example/example/MA35H0_Registers.xml"

bases = [
    ("TIMER2", "0x40510000"),
    ("TIMER3", "0x40510100"),
    ("TIMER4", "0x40520000"),
    ("TIMER5", "0x40520100"),
    ("TIMER6", "0x40530000"),
    ("TIMER7", "0x40530100"),
    ("TIMER8", "0x40540000"),
    ("TIMER9", "0x40540100"),
    ("TIMER10", "0x40550000"),
    ("TIMER11", "0x40550100"),
]

template = """
    <!-- {name} : 타이머 {num} -->
    <RegisterGroup description="Timer Controller {num}" name="{name}" start="{base}">
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

if "TIMER2" not in content:
    extra_xml = ""
    for name, base in bases:
        num = name.replace("TIMER", "")
        extra_xml += template.format(name=name, num=num, base=base)
    
    content = content.replace("</Processor>", extra_xml + "</Processor>")
    with open(xml_file, "w") as f:
        f.write(content)
    print("Success")
else:
    print("Already exists")
