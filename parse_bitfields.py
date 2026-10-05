import re
import os
import xml.etree.ElementTree as ET

xml_file = "/home/mymy49/git-repository/examples/NuMaker-HMI-MA35H0-A1_example/example/MA35H0_Registers.xml"
clk_header = "/home/mymy49/Downloads/MA35H0_NonOS_BSP-master/Library/Device/Nuvoton/MA35H0/Include/clk_reg.h"
timer_header = "/home/mymy49/Downloads/MA35H0_NonOS_BSP-master/Library/Device/Nuvoton/MA35H0/Include/timer_reg.h"

def parse_header(filepath, prefix):
    # Returns dict: { "REG_NAME": [ {"name": field, "start": s, "size": sz, "desc": desc}, ... ] }
    reg_dict = {}
    current_reg = None
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        # Look for: * @var CLK_T::CLKSEL0
        m_reg = re.search(r'@var\s+([A-Z0-9_]+)_T::([A-Z0-9_]+)', line)
        if m_reg:
            struct_name = m_reg.group(1)
            reg_name = m_reg.group(2)
            if struct_name == prefix:
                current_reg = reg_name
                if current_reg not in reg_dict:
                    reg_dict[current_reg] = []
            continue
            
        if current_reg:
            # Look for: * |[2:0]   |HCLKSEL   |HCLK Clock Source Select
            # Or:       * |[5]     |STCLKSEL  |...
            m_bit = re.search(r'\|\s*\[(\d+)(?::(\d+))?\]\s*\|\s*([A-Z0-9_]+)\s*\|(.*)', line)
            if m_bit:
                bit_high = int(m_bit.group(1))
                bit_low = int(m_bit.group(2)) if m_bit.group(2) else bit_high
                start = bit_low
                size = bit_high - bit_low + 1
                field_name = m_bit.group(3).strip()
                desc = m_bit.group(4).strip()
                
                # Clean up desc
                desc = desc.replace('"', "'").replace('<', '&lt;').replace('>', '&gt;')
                
                reg_dict[current_reg].append({
                    "name": field_name,
                    "start": start,
                    "size": size,
                    "desc": desc
                })
    return reg_dict

clk_fields = parse_header(clk_header, "CLK")
timer_fields = parse_header(timer_header, "TIMER")

# Update XML
tree = ET.parse(xml_file)
root = tree.getroot()

for group in root.findall("RegisterGroup"):
    gname = group.get("name")
    
    fields_dict = None
    if gname == "CLK":
        fields_dict = clk_fields
    elif gname.startswith("TIMER"):
        fields_dict = timer_fields
        
    if fields_dict:
        for reg in group.findall("Register"):
            rname = reg.get("name")
            # Remove existing BitFields just in case to avoid duplicates
            for bf in reg.findall("BitField"):
                reg.remove(bf)
                
            if rname in fields_dict:
                for bf in fields_dict[rname]:
                    bf_elem = ET.SubElement(reg, "BitField")
                    bf_elem.set("name", bf["name"])
                    bf_elem.set("start", str(bf["start"]))
                    bf_elem.set("size", str(bf["size"]))
                    bf_elem.set("description", bf["desc"])

# Write back without breaking the format too much, use a generic rough indentation
ET.indent(tree, space="    ", level=0)
tree.write(xml_file, encoding="utf-8", xml_declaration=False)

# Re-add doctype which ET removes
with open(xml_file, "r") as f:
    content = f.read()
content = "<!DOCTYPE Register_Definition_File>\n" + content
with open(xml_file, "w") as f:
    f.write(content)
print("Bitfields updated.")
