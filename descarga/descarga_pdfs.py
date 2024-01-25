
# Importar las paginas a Utilizar
import pdf_reader


# Importar librerias
import os
import requests

from bs4 import BeautifulSoup
from IPython.display import HTML
from urllib.parse import urljoin


# Here, provide the URL where are all the PDFs that you want to download are located.
url = "https://www.aerocivil.gov.co/autoridad-de-la-aviacion-civil/reglamentacion/rac"


# Here you must specify the folder where the PDFs will be downloaded.
folder_downloaded = 'racs_pdf_pagina'

# if you haven´t created that folder, here the folder will be created automatically whit the name written above.
folder_location = rf'/content/drive/MyDrive/FULL-Seminario/Proyectos/rac_gpt/racs/{folder_downloaded}'
if not os.path.exists(folder_location):os.mkdir(folder_location)



# Here the vraiable response countain all information about the page
response = requests.get(url)

# With BeautifulSoup library you can obtein data from HTML or XML, for this case we are obteining it for HTML dates
soup = BeautifulSoup(response.text, "html.parser")


# This part of the code checks for all PDF´s field in the page
for link in soup.select("a[href$='.pdf']"):

    # Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])

    print(filename)

    # Open the fields created above in binary mode.
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)


# Here is the list of the PDFs that have been downloaded
        
pdfs = os.listdir(folder_location)
print(f"The PDFs downloaded are:\n{pdfs}")

# With this code, you are avable to see the paths of the PDFs

path_pdf = []
[path_pdf.append(os.path.join(folder_location,rac)) for rac in pdfs]

print(f"\nThe PDFs path are:\n{path_pdf}")


# DIGITE LA PAGINA QUE QUIERE LEER

pag_re = 1

pag_re = path_pdf(pag_re)

num_pag = pdf_reader.reader(pag_re)
cont_pag =pdf_reader.extract(pag_re)

print(f("El PDF tiene {num_pag} paginas, el contenido de las paginas es: \n\n{cont_pag}"))
                   
