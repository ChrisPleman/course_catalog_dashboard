from pypdf import PdfReader as pr

reader = pr("pdfs\ccsf_fall-2025-credit-classes.pdf")



first_page = reader.pages[0].extract_text().split('\n')
# Contains the information about the context of the courses in this file
meta = first_page[0].split()
print(meta)

school = meta[2][4:]
are_credit_courses = True if meta[0] == 'CREDIT' else False
term = meta[1]
year = meta[2][:4]

print(school, are_credit_courses, term, year)
column_headers = first_page[1]

print(column_headers.split('  '))

font_sizes = []

def visitor_body(text, cm, tm, font_dict, font_size):
    font_sizes.append(font_size)
    
a = reader.pages[0]
a.extract_text(visitor_text=visitor_body)

print(set(font_sizes))



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