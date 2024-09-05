import scrapy
import csv


class KeywordSpider(scrapy.Spider):
    name = 'spider1'

    start_urls = [
        'https://concepto.de/que-es-la-filosofia/',
        'https://www.anipedia.net/perros/',
        'https://www.ecologiaverde.com/que-son-los-vegetales-3177.html',
    ]

    # La palabra que estamos buscando
    palabra = 'modo'

    def parse(self, response):

        texto = response.text.lower()

        ocurrencias = texto.count(self.palabra.lower())

        if ocurrencias > 0:
            yield {
                'url': response.url,
                'ocurrencias': ocurrencias
            }
# Configuración para guardar en CSV
FEEDS = {
    'resultados.csv': {
        'format': 'csv',
        'overwrite': True,
    },
}
