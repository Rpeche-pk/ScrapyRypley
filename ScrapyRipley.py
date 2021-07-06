from scrapy.item import Item
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Field
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.spiders import Spider
from twisted.python.compat import raw_input

from ScrapyRipleyLaptop import LaptopGamer


class Tecnologia(Item):
    titulo=Field()
    #precioNormal=Field()
    #precioDescuento=Field()




class LaptopGamer(CrawlSpider):
    name='laptop'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/80.0.3987.149 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 5
    }

    allowed_domains=["simple.ripley.com.pe"]


    user = raw_input("""Escriba una Opcion a realizar su consulta:
    monitores gamer
    componentes
    audifonos gamer
    teclado y mouse
    camaras web
    sillas gamer
    """)
    resultado = user.replace(' ', '-')

    start_urls=[f"https://simple.ripley.com.pe/tecnologia/computacion-gamer/{resultado}?source=menu"]
    download_delay=2

    rules = (
        Rule(
            LinkExtractor(
                allow=r'page=\d'
            ), follow=True, callback='parse_items'
        ),
    )


    def parse_items(self, response):
        sel=Selector(response)
        productos=sel.xpath("//div[@class='row']//div[@class='catalog-product-item catalog-product-item__container col-xs-6 col-sm-6 col-md-4 col-lg-4']")
        init = 0
        for producto in productos:

            tamano=len(productos)
            item= ItemLoader(Tecnologia(), producto)
            item.add_xpath('titulo',".//div[@class='catalog-product-details']/div[2]/text()")
            init+=1
            print("EXTAYENDO INFORMACION" +" "+str(init)+ " de " + str(tamano))
            if init == tamano:
                print("---------------------SE EXTRAJO LA INFORMACION CORRECTAMENTE :)---------------------------")
                print("---------------------SE EXTRAJO LA INFORMACION CORRECTAMENTE :)---------------------------")
            yield item.load_item()

    #print(f"--------------EXTRACCION TERMINADA: {resultado}----------------- ")



