import requests
from api import API_KEY, API_URl


def genrate_response(self,product_name,ingredients):

    url = API_URl

    ingredients = "Aqua, Glycerin, Cetearyl Alcohol, Isohexadecane, Isopropyl Palmitate, Paraffinum Liquidum, Glyceryl Stearate SE, Butyrospermum Parkii Butter, Dimethicone, Glyceryl Stearate, Theobroma Cacao Seed Butter, Cocos Nucifera Oil, Tocopheryl Acetate, Glyceryl Glucoside, Carbomer, Sodium Cetearyl Sulfate, Trisodium EDTA, Ethylparaben, Methylparaben, Phenoxyethanol, Sodium Hydroxide, Perfume, Ethylhexylglycerin, Linalool, Benzyl Alcohol, Coumarin, BHT, C15-19 Alkane"
    product_name = "Nivea body lotion"
    
    prompt = f"""this is ingredients list of a {product_name},
            tell me which item is good and bad in csv format: {ingredients},
            ouput should me in this format: Good: list, then Bad: list, and in last a Note: about classification of ingredients as good and bad"""

    payload = {
        "enable_google_results": False,
        "enable_memory": False,
        "input_text": prompt
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    print(response_data)

    return response_data['message']
