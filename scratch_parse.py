import xml.etree.ElementTree as ET

xml_file = 'xml_snapshots/260505_execute_5506_ass.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Codesys PLCopen XML often uses this namespace
namespace = {'ns': 'http://www.plcopen.org/xml/tc6_0200'}

print('--- POUs (Programs, Function Blocks, etc.) ---')
for pou in root.findall('.//ns:pou', namespace):
    name = pou.get('name')
    pou_type = pou.get('pouType')
    print(f'POU: {name}, Type: {pou_type}')

print('\n--- Global Variables ---')
for gvl in root.findall('.//ns:globalVars', namespace):
    gvl_name = gvl.get('name', 'Unnamed')
    print(f'GVL Name: {gvl_name}')
    for var in gvl.findall('.//ns:variable', namespace):
        name = var.get('name')
        type_elem = var.find('.//ns:type/*', namespace)
        if type_elem is not None:
            type_name = type_elem.tag.split('}')[-1]
            if type_name == 'derived':
                type_name = type_elem.get('name')
        else:
            type_name = 'Unknown'
        print(f'  {name}: {type_name}')

print('\n--- Local Variables ---')
for pou in root.findall('.//ns:pou', namespace):
    pou_name = pou.get('name')
    vars = pou.findall('.//ns:localVars/ns:variable', namespace)
    if vars:
        print(f'\nPOU: {pou_name}')
        for var in vars:
            name = var.get('name')
            type_elem = var.find('.//ns:type/*', namespace)
            if type_elem is not None:
                type_name = type_elem.tag.split('}')[-1]
                if type_name == 'derived':
                    type_name = type_elem.get('name')
            else:
                type_name = 'Unknown'
            print(f'  {name}: {type_name}')
