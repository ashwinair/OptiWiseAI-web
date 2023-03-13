import requests
from optiwise.api import API_KEY, API_URl

class ChatSonic:

    def __init__(self,product_type,ingredients):
            self.product_type = product_type
            self.ingredients = ingredients

    def generate_response(self):
        prompt = f"""this is ingredients list of a {self.product_type},
            tell me which item is good and bad in csv format: {self.ingredients},
            output should me in this format: Good: list, then Bad: list, and in last a Note: about classification of ingredients as good and bad"""

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

        response = requests.post(API_URl, json=payload, headers=headers)
        response_data = response.json()
        #print(response_data)
        message = response_data['message']
        good_bad_note_list = message.split('Bad:')

        good_list = good_bad_note_list[0].replace('Good:', '').strip().split('\n')
        bad_note_list = good_bad_note_list[1].strip().split('Note:')
    
        if len(bad_note_list) > 1:
            bad_list = bad_note_list[0].strip().split('\n')
            note = bad_note_list[1].strip()
        else:
            bad_list = bad_note_list[0].strip().split('\n')
            note = bad_note_list[1].strip()

        result_dict = {'Good': good_list, 'Bad': bad_list, 'Note': note}

        return result_dict

    # def genrate_response(self):
        
    #     prompt = f"""this is ingredients list of a {self.product_type},
    #         tell me which item is good and bad in csv format: {self.ingredients},
    #         ouput should me in this format: Good: list, then Bad: list, and in last a Note: about classification of ingredients as good and bad"""

    #     payload = {
    #         "enable_google_results": False,
    #         "enable_memory": False,
    #         "input_text": prompt
    #     }

    #     headers = {
    #         "accept": "application/json",
    #         "content-type": "application/json",
    #         "X-API-KEY": API_KEY
    #     }

    #     response = requests.post(API_URl, json=payload, headers=headers)
    #     response_data = response.json()
    #     message = response.json()['message']
    #     good_bad_list = message.split('Bad:')

    #     good_list = good_bad_list[0].replace('Good:', '').strip().split('\n')
    #     bad_list = good_bad_list[1].strip().split('\n')

    #     note = message.split('Note:')[1].strip()

    #     result_dict = {'Good': good_list, 'Bad': bad_list, 'Note': note}

    #     return result_dict
