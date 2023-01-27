import json
from flask import Flask, request, render_template

"""
Web page offers full country information based on a given country name.

-Uploading the data file that contain a list of dictionaries with each country informations.
-Then using flask API that reciving a 'POST' request with the country name from HTML(user).
-Flask will render the template with the data (the template will be stored in the "templates" directory).
-In the application, we will use templates to render HTML which will find the country info. and display in the user's browser.
"""

data = json.load(open('debug.json'))

app = Flask(__name__)

@app.route("/get", methods= ['GET' ,'POST'])
def get_data():
    country_name=request.form.to_dict()
    name=country_name["name"]
    
    return render_template("index.html", name=name, data=data)


if __name__=="__main__":
    app.run(use_reloader = True,debug=True)
