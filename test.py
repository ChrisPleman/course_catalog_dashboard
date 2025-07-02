from pypdf import PdfReader as pr
# At some point I'm going to have to import this
import pandas as pd
import numpy as np

reader = pr("pdfs\ccsf_fall-2025-credit-classes.pdf")



first_page = reader.pages[0].extract_text().split('\n')
# Contains the information about the context of the courses in this file
meta = first_page[0].split()
print(meta)

# Weird space between hard coding and kind of not?
meta = {
    'school': meta[2][4:],
    'are_credit_courses': True if meta[0] == 'CREDIT' else False,
    'term': meta[1],
    'year': meta[2][:4] 
}

print(meta)


column_headers = [
    'CRN',
    'SEC',
    'TYPE',
    'DAYS',
    'TIMES',
    'DATES',
    'LOCATION',
    'CAMPUS',
    'INSTRUCTOR'
]

lines = []
font_sizes = []
idk = []

# So, based on the description that "tm" refers to the text space matrix, where the first four contain the rotation/scaling and the last two contain the translation
# alongside the fact that the tm only has the first and fourth element filled out, I am going to consider the fourt element the "font size" and see where that takes me
# For greater clarity, I am choosing the 4th element, because "scaling" was included after "rotation" in the description
# Here is the link: https://pypdf.readthedocs.io/en/stable/user/extract-text.html


# def visitor_body(text, cm, tm, font_dict, font_size):
#     # One thing I can consider is that font size is more important for identifying headers, and there are less of those so I will try that filtering
    
#     # Now let's make sure the text isn't empty
#     if tm[3] < 2: #text not in  ('', ' ', '\n'): # I'll use regex later
#         lines.append(repr(text))
#         font_sizes.append(tm[3])
#     # cm = np.array(cm)
#     # tm = np.array(tm)
#     # idk.append((tm * cm))
    

    
a = reader.pages[0]
# a.extract_text(visitor_text=visitor_body, extraction_mode="plain")

# print(set(font_sizes))

# # Checking number of lines this approach sees
# print(len(font_sizes))

# for line_num, (line, font_size) in enumerate(zip(lines, font_sizes)):
#     print(f"{line_num}: ({font_size}) - {line}")
    




# for i, page in enumerate(reader.pages):
#     extracted_text = page.extract_text(
#         extraction_mode="layout"
#     )
#     # print(type(extracted_text)) -> str
#     extracted_text_list = extracted_text.split('\n')
#     print(len(extracted_text_list))
#     for j, extracted_line in enumerate(extracted_text_list):
#         print(extracted_line)
#         if j >= 1:
#             break
#     break



# Let's see what each font size looks like

font_limit = 0
_lines = []        
_dict = {}

def visitor_body(text, cm, tm, font_dict, font_size):
    if tm[3] == font_limit: 
        if text not in  ('', ' ', "'  '", '\n'): # I'll use regex later
            # print("font size:", tm[3])
            # print("text:", text)
            _lines.append(repr(text))

for i in range(20):
    font_limit = i
    # print("font limit:", font_limit)
    a.extract_text(visitor_text=visitor_body, extraction_mode="plain")
    _list = _lines.copy()
    _dict[i] = (len(_list), _list)
    _lines = []
    
for k, v in _dict.items():
    if v[0] > 0:
        print(k, v)
        
# Basically this has shown me the following:
# Font 9: Paragraph text, specific course information (CRN, SEC, etc.)
# Font 11: Footer data
# Font 14: Department(?), course title, number of units
# Font 16: Main title of the document

# 