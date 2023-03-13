import openai
from optiwise.api import OPENAI_API_KEY


class ChatGPT:

    def __init__(self, product_type, ingredients):
            self.product_type = product_type
            self.ingredients = ingredients
            openai.api_key = OPENAI_API_KEY
            # Set the model and parameters
            self.model_engine = 'gpt-3.5-turbo'
            #"text-davinci-003"
            self.temperature = 0.7
            self.max_tokens = 100
            # Define the prompt for the model
            self.prompt = (
                 f"""ingredients list of a product type {self.product_type}, tell me which item is good and bad in genral: {self.ingredients}
                    content in json response should be like this example: \n\n\n\nGood: Jojoba Seed Oil, Sunflower Seed Oil\n\nBad: none\n\ninfo: All the ingredients listed are considered good and beneficial for hair.
                    """
            )
        

    def generate_ingredients_classification(self):
            # response = openai.Completion.create(
            #     engine=,
            #     prompt=,
            #     temperature=self.temperature,
            #     max_tokens=self.max_tokens,
            # )
            response = openai.ChatCompletion.create(model=self.model_engine, messages=[{"role": "user", "content": self.prompt}])
            print(response)
            

            ingredients_dict = {}
            #print(response)
            output_list = response['choices'][0]["message"]["content"].strip().split("\n\n")
            print(output_list)
            ingredients_dict["good_ingredients"] = [x.strip()
                                                for x in output_list[0].split(":")[1].split(",")]
            print('good:' , ingredients_dict["good_ingredients"])
            ingredients_dict["bad_ingredients"] = [x.strip()
                                               for x in output_list[1].split(":")[1].split(",")]
            print('bad:' , ingredients_dict["bad_ingredients"])
            ingredients_dict["information"] = {}

            # for info in output_list[2:]:
            #     ingredient, description = info.split(":")
            #     ingredients_dict["information"][ingredient.strip()
            #                                 ] = description.strip()
            # #ingredients_dict["token_size"] = response.choices[0].text_length
            for info in output_list[2:]:
                information = info.split(':')
                ingredients_dict["information"] = information[1].strip()
            print('information:' , ingredients_dict["information"])
            
            return ingredients_dict


# # Define the route for the API
# @app.route("/classify-ingredients", methods=["POST"])
# def classify_ingredients():
#     # Get the ingredients list from the request
#     ingredients = request.form.get("ingredients")
#     prompt = f"this is ingredients list of a product, tell me which item is good and bad: {ingredients}. Output should be in this format: Good: list, then Bad: list, and in last a Note: about classification of ingredients as good and bad"


#     # Return the response as JSON
#     return jsonify(ingredients_dict)
