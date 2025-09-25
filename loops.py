#Check whether any filename appears more than once 

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.asv',
    'export.pdf',
    ] 
for file in file_list:
    if file_list.count(file) > 1:
        print("Duplicate found")
        break
    else :
        print("All files are unique")


