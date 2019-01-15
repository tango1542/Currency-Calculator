from flask import Flask, render_template, request
import requests
import os


app = Flask(__name__)
api_key=os.environ.get('APIKEY')


category = {'Euros':'EUR','British Pounds':'GBP','Japanese Yen':'JPY','Canadian Dollar':'CAD'}



@app.route('/')
def hello_world():


    return render_template('index.html',category=category)


@app.route('/convert',methods=['POST'])
def convert():


    amount = int(request.form['amount'])  #This gets the amount that the user puts in on the index page
    print ("This is amount" + str(amount))


    currency = request.form['currencies']  #This is the currency that the user selects from the dropdown
    print ("This is currency " + currency)

    r = requests.get('https://openexchangerates.org/api/latest.json?app_id=' + api_key).json()
    curr = r['rates'][currency]   #This gets the selected rate from the json
    currency_rate = round(curr, 2)

    print ("This is the exchange rate" + str(currency_rate))

    total = amount * currency_rate
    total_convert = str(round(total, 2))   #Rounding to two decimal places


    curr_comp= [key for (key,value) in category.items() if value == currency]
    currency_printed=curr_comp.pop(0)
    print (curr_comp)
    print (currency_printed)

    return render_template("convert.html",total_convert=total_convert,amount=amount,currency=currency,currency_rate=currency_rate,print_name=currency_printed)



if __name__ == '__main__':
    app.run()
