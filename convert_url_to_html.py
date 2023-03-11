import requests
from bs4 import BeautifulSoup


def get_scrape_data(slef, product_link):

    # Replace "product_link" with your desired Amazon product link
    product_link = "https://www.amazon.co.uk/dp/B0BVG8J1JG/ref=sspa_dk_detail_2?psc=1&pf_rd_p=00b0073a-c363-4c4d-a2c8-d51ea12ea8c0&pf_rd_r=AV3F5R1J5ER12ZDNHD7F&pd_rd_wg=rX52B&pd_rd_w=t6kaS&content-id=amzn1.sym.00b0073a-c363-4c4d-a2c8-d51ea12ea8c0&pd_rd_r=0b44d045-1810-4b15-99b3-94c098265fc0&s=beauty&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy"
    # "https://www.amazon.in/Biotique-Morning-Nectar-Flawless-Lotion/dp/B006NVDWGE?ref_=ast_sto_dp&th=1"
    # "https://www.amazon.in/TRESemme-Keratin-Smooth-Shampoo-1000ml/dp/B07L3ZCJ53/?_encoding=UTF8&pd_rd_w=EqWBN&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=XW1FB9N8VTPYZYWC3SQT&pd_rd_wg=lTOmx&pd_rd_r=fb46761e-2fb5-4f22-b768-eada7175c6f7&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"

    # Make a GET request to the product page
    response = requests.get(product_link)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section of the product page that contains the list of ingredients
    ingredients_section = soup.find_all("div", {"id": "important-information"})

    # Find the list of ingredients within the ingredients section

    ingredients_section_list = []
    # Print the list of ingredients
    # for ingredients in ingredients_section:
    #  print(ingredients.get_text().strip())

    # Print the list of ingredients
    print("List of ingredients:")
    for ingredients in ingredients_section:
        ingredients_lists = ingredients.find_all(
            "div",  attrs={"class": "a-section content"})
        for ingredient in ingredients_lists:
            arr = ingredient.text.split(":")
            ingredients_section_list.append(arr)

return ingredients_section_list

# if == 0 or 1 then no data available
# if <=5 then looks like not enough data available
# print(l[1][1])
