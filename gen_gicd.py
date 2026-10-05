import sys

out = []
out.append('    <RegisterGroup description="Generic Interrupt Controller Distributor (GICD)" name="GICD" start="0x50801000">')
out.append('        <Register access="Read/Write" description="Distributor Control Register" name="GICD_CTLR" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x0">')
out.append('            <BitField description="Enable Group 0" name="EnableGrp0" size="1" start="0" />')
out.append('            <BitField description="Enable Group 1" name="EnableGrp1" size="1" start="1" />')
out.append('        </Register>')
out.append('        <Register access="ReadOnly" description="Interrupt Controller Type Register" name="GICD_TYPER" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x4" />')
out.append('        <Register access="ReadOnly" description="Distributor Implementer Identification Register" name="GICD_IIDR" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0x8" />')

# Arrays (0 to 5) for 1-bit per IRQ registers (192 IRQs)
for i in range(6):
    out.append(f'        <Register access="Read/Write" description="Interrupt Group Register {i}" name="GICD_IGROUPR{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x080 + i*4)}" />')
for i in range(6):
    out.append(f'        <Register access="Read/Write" description="Interrupt Set-Enable Register {i}" name="GICD_ISENABLER{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x100 + i*4)}" />')
for i in range(6):
    out.append(f'        <Register access="Read/Write" description="Interrupt Clear-Enable Register {i}" name="GICD_ICENABLER{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x180 + i*4)}" />')
for i in range(6):
    out.append(f'        <Register access="Read/Write" description="Interrupt Set-Pending Register {i}" name="GICD_ISPENDR{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x200 + i*4)}" />')
for i in range(6):
    out.append(f'        <Register access="Read/Write" description="Interrupt Clear-Pending Register {i}" name="GICD_ICPENDR{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x280 + i*4)}" />')

# Priority and Target (4 IRQs per register, 0 to 47 for 192 IRQs)
for i in range(48):
    out.append(f'        <Register access="Read/Write" description="Interrupt Priority Register {i}" name="GICD_IPRIORITYR{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x400 + i*4)}" />')
for i in range(48):
    out.append(f'        <Register access="Read/Write" description="Interrupt Processor Target Register {i}" name="GICD_ITARGETSR{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0x800 + i*4)}" />')

# Config (16 IRQs per register, 0 to 11 for 192 IRQs)
for i in range(12):
    out.append(f'        <Register access="Read/Write" description="Interrupt Configuration Register {i}" name="GICD_ICFGR{i}" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+{hex(0xC00 + i*4)}" />')

out.append('        <Register access="WriteOnly" description="Software Generated Interrupt Register" name="GICD_SGIR" reset_mask="0xFFFFFFFF" reset_value="0x00000000" size="4" start="+0xF00" />')
out.append('    </RegisterGroup>')

with open("gicd_block.xml", "w") as f:
    f.write("\n".join(out) + "\n")
