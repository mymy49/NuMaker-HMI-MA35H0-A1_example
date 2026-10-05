import os

xml_file = "/home/mymy49/git-repository/examples/NuMaker-HMI-MA35H0-A1_example/example/MA35H0_Registers.xml"

clk_xml = """
    <!-- CLK : Clock Controller -->
    <RegisterGroup description="Clock Controller" name="CLK" start="0x40460200">
        <Register access="Read/Write" description="System Power-down Control Register" name="PWRCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0000"/>
        <Register access="Read/Write" description="AXI and AHB Device Clock Enable Control Register 0" name="SYSCLK0" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0004"/>
        <Register access="Read/Write" description="AXI and AHB Device Clock Enable Control Register 1" name="SYSCLK1" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0008"/>
        <Register access="Read/Write" description="APB Devices Clock Enable Control Register 0" name="APBCLK0" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x000C"/>
        <Register access="Read/Write" description="APB Devices Clock Enable Control Register 1" name="APBCLK1" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0010"/>
        <Register access="Read/Write" description="APB Devices Clock Enable Control Register 2" name="APBCLK2" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0014"/>
        <Register access="Read/Write" description="Clock Source Select Control Register 0" name="CLKSEL0" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0018"/>
        <Register access="Read/Write" description="Clock Source Select Control Register 1" name="CLKSEL1" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x001C"/>
        <Register access="Read/Write" description="Clock Source Select Control Register 2" name="CLKSEL2" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0020"/>
        <Register access="Read/Write" description="Clock Source Select Control Register 3" name="CLKSEL3" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0024"/>
        <Register access="Read/Write" description="Clock Source Select Control Register 4" name="CLKSEL4" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0028"/>
        <Register access="Read/Write" description="Clock Divider Number Register 0" name="CLKDIV0" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x002C"/>
        <Register access="Read/Write" description="Clock Divider Number Register 1" name="CLKDIV1" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0030"/>
        <Register access="Read/Write" description="Clock Divider Number Register 2" name="CLKDIV2" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0034"/>
        <Register access="Read/Write" description="Clock Divider Number Register 3" name="CLKDIV3" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0038"/>
        <Register access="Read/Write" description="Clock Divider Number Register 4" name="CLKDIV4" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x003C"/>
        <Register access="Read/Write" description="Clock Output Control Register" name="CLKOCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0040"/>
        <Register access="ReadOnly" description="Clock Status Monitor Register" name="STATUS" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0050"/>
        <Register access="Read/Write" description="CA-PLL Control Register 0" name="PLL0CTL0" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0060"/>
        <Register access="Read/Write" description="Clock Fail Detector Control Register" name="CLKDCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x00C0"/>
        <Register access="Read/Write" description="Clock Fail Detector Status Register" name="CLKDSTS" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x00C4"/>
        <Register access="Read/Write" description="Clock Frequency Detector Upper Boundary Register" name="CDUPB" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x00C8"/>
        <Register access="Read/Write" description="Clock Frequency Detector Lower Boundary Register" name="CDLOWB" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x00CC"/>
        <Register access="Read/Write" description="Clock Filter Control Register" name="CKFLTRCTL" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x00D0"/>
    </RegisterGroup>
"""

with open(xml_file, "r") as f:
    content = f.read()

if '<RegisterGroup description="Clock Controller" name="CLK"' not in content:
    content = content.replace("</Processor>", clk_xml + "</Processor>")
    with open(xml_file, "w") as f:
        f.write(content)
    print("Success")
else:
    print("Already exists")
