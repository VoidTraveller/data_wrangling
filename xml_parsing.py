from lxml import etree
import csv

filename = "U6_FRED_data"

xml_source_file = open(filename + '.xml', 'rb')

xml_doc = etree.parse(xml_source_file)

document_root = xml_doc.getroot()

print(etree.tostring(document_root))

if etree.iselement(document_root):
    output_file = open('xml_' + filename + '.csv', 'w')
    output_writer = csv.writer(output_file)
    
    output_writer.writerow(document_root[0].attrib.keys())
    
    for child in document_root:
        output_writer.writerow(child.attrib.values())
    
    output_file.close()
    