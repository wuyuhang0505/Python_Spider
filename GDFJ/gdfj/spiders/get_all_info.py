'''
Created on 

@author: hadoop
'''
from bs4 import BeautifulSoup
class get_all_info:
#get the page information
    
    def __init__(self,soup):
        self.soup = soup    
    def get_city(self):
        search_list=self.soup.select("#shle_city" )
        soup= BeautifulSoup(str(search_list[0]), 'lxml')
        return soup.input.attrs['value']

    def get_region(self):
        search_list=self.soup.select("#shle_region" )
        soup= BeautifulSoup(str(search_list[0]), 'lxml')
        return soup.input.attrs['value']

    def get_district_name(self):
        search_list=self.soup.select("#shle_region" )
        soup= BeautifulSoup(str(search_list[0]), 'lxml')
        return soup.input.attrs['value']

    def get_title(self):
        search_list=self.soup.find_all(id="houseTitle")
        soup = BeautifulSoup(str(search_list[0]), 'lxml')
        return soup.select('h1')[0].get_text()

    def get_house_desc(self):
        search_list=self.soup.find_all(id="hdesc")
        soup = BeautifulSoup(str(search_list[0]), 'lxml')
        s=soup.select('div')[0].get_text()
        return s.replace('\n','')

    def get_house_infor(self):
        search_list=self.soup.select('li[class="clearfix"]')
        s=''
        for item in range(len(search_list)):
            soup= BeautifulSoup(str(search_list[item]), 'lxml')
            s=s+soup.select('li')[0].get_text()
        return s.replace('\n',' ')

    def get_contact(self):
        search_list=self.soup.find_all("div", class_="bk4")
        soup = BeautifulSoup(str(search_list[0]), 'lxml')
        return soup.select('span')[0].get_text()

    def get_phone_number(self):
        search_list=self.soup.find_all("div", class_="bk4")
        soup = BeautifulSoup(str(search_list[0]), 'lxml')
        return soup.select('span')[1].get_text() 
    def update_time(self):
        search_list=self.soup.find_all("div", class_="fr")
        soup = BeautifulSoup(str(search_list[0]), 'lxml')
        result=soup.select('div')[0].get_text()
        return result.replace('\n',' ')
    def get_img_url(self):
        value=[]
        def has_class_but_no_id(tag):
            return tag.has_attr('name') and tag.has_attr('data-original')
        search_list=self.soup.find_all(has_class_but_no_id)
        for i in range(len(search_list)):
            soup = BeautifulSoup(str(search_list[i]), 'lxml')
            v= soup.img.attrs['data-original']
            value.append(v)
        return value 

