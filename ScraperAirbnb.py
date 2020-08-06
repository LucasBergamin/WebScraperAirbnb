import matplotlib.pyplot
from bs4 import BeautifulSoup
import requests

lugares = []
valores = []
num = 0
convertendo = ""
convertendo1 = 0
desc = ""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) '
                  'Version/9.0.2 Safari/601.3.9'}
url = "https://www.airbnb.com.br/s/Ilhabela/homes?refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&place_id=ChIJUYm14aGZ0pQRIqNLP66xHNs&source=structured_search_input_header&search_type=autosuggest"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
for item in soup.select('[itemprop=itemListElement]'):
    try:
        print('----------------------------------------')
        print(item.select('a')[0]['aria-label'])
        descricao = item.select('a')[0]['aria-label']

        lugares.insert(num, item.select('a')[0]['aria-label'])
        print(item.select('._1p7iugi')[0].get_text())
        valor = item.select('._1p7iugi')[0].get_text()
        for n in valor:
            try:
                int(n)
                convertendo += n
            except:
                continue
        convertendo1 = int(convertendo)
        valores.insert(num, convertendo1)
        convertendo1 = 0
        convertendo = ""
        num = num + 1

    except Exception as e:
        # raise e
        print('')

matplotlib.pyplot.plot(lugares, valores)
matplotlib.pyplot.title('Tabela variação de valores - Ilhabela')
matplotlib.pyplot.show()

