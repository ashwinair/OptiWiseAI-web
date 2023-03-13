import requests
from bs4 import BeautifulSoup
import cloudscraper

class ProductDetails:
    
    def __init__(self,product_link):
        self.product_link = product_link
        #print(self.product_link)
        #response = requests.get(self.product_link)
        # Parse the HTML content using BeautifulSoup
        #print(response)
        #scraper = cloudscraper.create_scraper(delay=10)  # returns a CloudScraper instance
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        response = requests.get(self.product_link,headers=headers)
        #print(response.status_code) 
        self.soup = BeautifulSoup(response.text, "html.parser")
        print('-----------------')
        #print('html:', self.soup)
    # def get_html(self):
        # Replace "product_link" with your desired Amazon product link
        # "https://www.amazon.in/Biotique-Morning-Nectar-Flawless-Lotion/dp/B006NVDWGE?ref_=ast_sto_dp&th=1"
        # "https://www.amazon.in/TRESemme-Keratin-Smooth-Shampoo-1000ml/dp/B07L3ZCJ53/?_encoding=UTF8&pd_rd_w=EqWBN&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=XW1FB9N8VTPYZYWC3SQT&pd_rd_wg=lTOmx&pd_rd_r=fb46761e-2fb5-4f22-b768-eada7175c6f7&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
        # Make a GET request to the product page#return soup
    
    def get_information_section(self):
        # Find the section of the product page that contains the list of ingredients
        information_section = self.soup.find_all("div", {"id": "important-information"})
        # Find the list of ingredients within the ingredients section

        ingredients_list = []
        safety_information = []
        directions_to_use = []
        # Print the list of ingredients
        print("List of ingredients:")
        for info in information_section:
            all_info_lists = info.find_all(
            "div",  attrs={"class": "a-section content"})
            for particular_list in all_info_lists:
                arr = particular_list.text.strip().split(":")
                if arr[0] == "Ingredients":
                    ingredients_list = arr[1]
                elif arr[0] == "Safety Information":
                    safety_information = arr[1]
                elif arr[0] == "Directions":
                    directions_to_use = arr[1]  

        return {'Ingredients': ingredients_list, "Safety Information": safety_information, "Directions": directions_to_use}

    def get_product_name_and_type(self):

        product_name_html = self.soup.find_all("div", {"id": "titleSection"})

        for info in product_name_html:
            product_name = info.find("span",  attrs={"id": "productTitle"})

        product_type_html = soup.find_all("div", {"id": "detailBullets_feature_div"})
        other_details = []
        for details in product_type_html:
            details_ul = details.find_all("ul", {"class":"a-unordered-list"})
            for ul in details_ul:
                details_li = ul.find_all("li")
                for li in details_li:
                    other_details.append(li.text.replace("\u200f\n", "").replace("\u200e\n", "").replace("\n",""))

        print(other_details)
        return

    
