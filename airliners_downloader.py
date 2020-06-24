
import os

filename = "search?keywords=a320"
urlBase = "https://www.airliners.net/"
pages = 20
divItem = "ps-v2-results-display-detail-col photo"


def htmlDownload():
    for i in range(0,pages):
        urlBusca = urlBase + filename + "&page=" + str(i+1);
        os.system("wget " + '"' + urlBusca + '"')

def paginaImagem(urlPagina):
    os.system("wget -O crivo " + urlBase + urlPagina)
    htmlfile = open("crivo", 'r')

    for line in htmlfile:
        if line.find("property=\"og:image\"") > 0:
            img_path = line[35:line.find('?')]      #<meta property="og:image" content="https://imgproc.airliners.net/photos/airliners/5/2/6/6030625.jpg?v=v4ad08919b7e" />
            os.system("wget " + img_path)

    htmlfile.close()

def paginaBusca(filename):

    htmlfile = open(filename, 'r')

    get_href = False
    for line in htmlfile:
        if line.find(divItem) > 0:
            get_href = True
        if get_href: 
            if line.find("<a href") > 0:
                url_imagem = line[line.find("<a href")+10:len(line)-3]
                paginaImagem(url_imagem)
                get_href = False


    htmlfile.close()
    #os.system("rm " + filename)

if not os.path.exists(filename + "&page=" + str(1)):
    htmlDownload()

for i in range(0,pages):
    paginaBusca(filename + "&page=" + str(i+1))

