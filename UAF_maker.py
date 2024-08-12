import os
import docx

input_folder = 'UAF_Template'
output_folder = 'UAF_Student_B'
filename = 'template.docx'

first_name = ("Alex","Jamie","Jordan","Casey","Taylor","Morgan","Riley")
last_name = ("Smith","Johnson","Brown","Davis","Miller","Wilson","Moore")
CRSID = ("abc12","xyz34","jkl56","mno78","pqr90","stu23","vwx45")
position = ("MASt","NST3AS","NST3AS","NST3AS","NST3AS","NST3AS","NST3AS")
duration = "09/10/2024"
room = ("")
initials = ('AS', 'JJ', 'JB', 'CD', 'TM', 'MW', 'RM')
UID = ("12345","67890","11223","44556","77889","99001","22334")
ticket_number = ("100001", "100002", "100003", "100004", "100005", "100006", "100007")

    
def replace_words(docx_path, i):
    try:
        doc = docx.Document(docx_path)
    except docx.opc.exceptions.PackageNotFoundError:
        print(f'Error: Could not open {docx_path}')
        return

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.text = run.text.replace('fn', first_name[i - 1])
            run.text = run.text.replace('ln', last_name[i - 1])
            run.text = run.text.replace('crs1d', CRSID[i - 1])
            run.text = run.text.replace('pos1t1on', position[i-1])
            run.text = run.text.replace('l3ngth', duration)
            run.text = run.text.replace('r00m', "")
            run.text = run.text.replace('1n1t1al', initials[i - 1])
            run.text = run.text.replace('u1d', UID[i - 1])
            run.text = run.text.replace('t1cket', ticket_number[i - 1])

    modified_docx_path = os.path.join(output_folder, f'UAF_{first_name[i - 1]}_{last_name[i - 1]}.docx')
    doc.save(modified_docx_path)
    print(f'Replaced placeholders in {docx_path} and saved as {modified_docx_path}')



#go through each document in the input folder and run the replace_words function
for i in range(len(first_name)):
    docx_path = os.path.join(input_folder, filename)
    replace_words(docx_path, i)
    print(f'Finished processing {docx_path}\n')

print("Fully completed script\n")






    

