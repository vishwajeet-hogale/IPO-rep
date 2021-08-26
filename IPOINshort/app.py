from flask import Flask
import pandas 
from flask import render_template,request,redirect,url_for
# import t5_textsumm as t5
# import livemint as lm
app = Flask(__name__)

filename = 'afrsumm.csv'
data = pandas.read_csv(filename, header=0)
data=data.dropna()

@app.route('/')
def index():
    
    myData = list(data.values)
    
    return render_template('index.html', contacts=myData)

@app.route('/page/<id>',methods=["GET"])
def page(id):
    row=data[data['id']==int(id)].values
    print(row)
    return render_template('page.html',contacts=row)
    



if __name__ == "__main__":
    app.run(debug=True)