import os
import glob
import cv2
import pytesseract 

from pdf2image import convert_from_path

pdf_name = 'SafetyNet'
pdf_source_file = pdf_name+'.pdf'

if os.path.isdir(pdf_name) == False:
    target_folder = os.mkdir(pdf_name)
    
pages = convert_from_path(pdf_source_file, 300)

for page_num, page in enumerate(pages):
    filename = os.path.join(pdf_name,'p'+str(page_num)+'.png')
    # print(filename)
    page.save(filename, 'PNG')

for img_file in glob.glob(os.path.join(pdf_name, '*.png')):
    temp_file = img_file.replace('\\','.')
    text_filename = temp_file.split('.')[1]
    
    output_file = open(os.path.join(pdf_name,text_filename + '.txt'), 'w')
    
    img = cv2.imread(img_file)
    converted_text = pytesseract.image_to_string(img)
    output_file.write(converted_text)
    
    output_file.close()
 