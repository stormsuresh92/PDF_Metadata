from PyPDF2 import PdfFileReader
import pandas as pd

data = []
file = ['main.pdf', 'poveda2017.pdf', 'tasian2017.pdf', 'oncotarget-11-992.pdf', 'NEJMoa2034577.pdf']
for item in file:
    pdf_file = open(str(item), 'rb')
    pdf = PdfFileReader(pdf_file)
    pdf_info = pdf.getDocumentInfo()
    try:
        pdfname = item
    except:
        pdfname = ''
    try:
        Title = pdf_info.title
    except:
        Title = ''
    try:
        Author = pdf_info.author
    except:
        Author = ''
    try:
        Doi = pdf_info['/doi']
    except:
        Doi = ''
    try:
        Pages = pdf.numPages
    except:
        Pages = ''
    try:
        Subject = pdf_info.subject
    except:
        Subject = ''
    try:
        Keywords = pdf_info['/Keywords']
    except:
        Keywords = ''
    try:
       Creation_Date = pdf_info['/CreationDate']
    except:
        Creation_Date = ''
    try:
        Creator = pdf_info.creator
    except:
        Creator = ''
    try:
        Producer = pdf_info.producer
    except:
        Producer = ''
        
    dic = {
        'PDFName':pdfname,
        'Title':Title,
        'Author':Author,
        'Doi':Doi,
        'Pages':Pages,
        'Subject':Subject,
        'Keywords':Keywords,
        'Creation_Date':Creation_Date,
        'Creator':Creator,
        'Producer':Producer
    }
    data.append(dic)

df = pd.DataFrame(data)
df.to_csv('Metadata.csv', index=False)
print('::::::::::::::::::::')
print('File downloaded')

