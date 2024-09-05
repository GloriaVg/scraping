import scrapy


class KeywordSpider(scrapy.Spider):
    name = "spider1"

    start_urls = [
        'https://concepto.de/que-es-la-filosofia/',
        'https://www.anipedia.net/perros/,'
        'https://uptecamac.edomex.gob.mx/',
    ]

    def parse(self, response):

        keyword = 'Alumnos'

        if keyword in response.text:
            yield {
                'url': response.url,
                'keyword_found': True,
            }
        else:
            yield {
                'url': response.url,
                'keyword_found': False,
            }
