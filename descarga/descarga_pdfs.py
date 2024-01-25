import os
import requests

from bs4 import BeautifulSoup
from IPython.display import HTML


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


pdfs = os.listdir(folder_location)
print(f"The PDFs downloaded are:\n{pdfs}")

path_pdf = []
[path_pdf.append(os.path.join(folder_location,rac)) for rac in pdfs]

print(f"\nThe PDFs path are:\n{path_pdf}")


