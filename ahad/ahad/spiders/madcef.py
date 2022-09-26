
import scrapy


class MadchefAhad2(scrapy.Spider):
    name = 'mad_ahad_dtls'
    allowed_domains = ['www.madchef.com.bd']
    start_urls = ['https://madchef.com.bd/contact']


    def parse(self, response):
        branch_n= response.xpath('//div[@class="branch-name "]//text()').getall()
        branch_ph= response.xpath('//div[@class="branch-phone"]//text()').getall()
        branch_ad= response.xpath('//div[@class="branch-address"]//text()').getall()
        #yield the specific tag and storing the whole data into a specific key
        yield{
               'b_name':branch_n,
               'b_phone':branch_ph,
               'b_address':branch_ad
                
            }
        
        #loop through branch
        
        for menu in response.xpath('//div[@class="branch "]'):
            yield {
                'branch_name': menu.xpath('normalize-space(.//div[@class="branch-name "]//text())').extract_first(),  
                'branch_phone': menu.xpath('.//div[@class="branch-phone"]//text()').extract(), 
                'branch_address': menu.xpath('.//div[@class="branch-address"]//text()').extract(),
                
                #//div[not(@class="cls")]
                                                                                   
            }
        