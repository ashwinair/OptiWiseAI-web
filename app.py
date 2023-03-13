
from flask import Flask, render_template, request
from product_details import ProductDetails
#from optiwise.chat_sonic import ChatSonic
from optiwise.chat_gpt import ChatGPT

app = Flask(__name__, template_folder='template', static_folder='static')

# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])#, methods=['POST']
def perform_url_actions():git st

    url = request.form['url']
    pro_details = ProductDetails(url)
    
    list_of_info = pro_details.get_information_section()

    #product_name = product_details.get_product_name_and_type()
    product_type = "face wash"
    ingredients = list_of_info.get('Ingredients')
    #print(list_of_info)
    safety_information = list_of_info.get('Safety Information')
    directions = list_of_info.get('Directions')
    res = {"good_ingredients" : ingredients}
    if len(ingredients) <= 1:
        #return not enough details :(
        print(ingredients)
        ingredients = "Not enough data available"
        print(ingredients)
    else:
        #optiWise = ChatSonic(product_type, ingredients)
        print("here goes the money")
        optiWise = ChatGPT(product_type, ingredients)
        result = optiWise.generate_ingredients_classification()
        #response = optiWise.generate_response() #it will return dict 
        #have to refine data and process nicely
        # print(safety_information)
        # print(directions)
        # print(response)
        return result
    return res
    

if __name__ == '__main__':
    app.run(debug=True)
