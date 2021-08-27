from flask import Flask
import pymongo
import pandas 
from flask import render_template,request,redirect,url_for
import services
# import t5_textsumm as t5
# import livemint as lm
app = Flask(__name__)

filename = 'afrsumm.csv'
data = pandas.read_csv(filename, header=0)
data=data.dropna()
mongo = pymongo.MongoClient("mongodb+srv://vishwajeet:Mjklop@cluster0.pkcgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = mongo["Blood-Bank"]
@app.route('/')
def index():
    
    # myData = list(data.values)
    news_data=services.get_data()
    myData = []
    for i in news_data:
        t = []
        t.append(i["id"])
        t.append(i["title"])
        t.append(i["link"])
        t.append(i["publish_date"])
        t.append(i["scraped_date"])
        t.append(i["text"])
        t.append(i["summary"])
        myData.append(t)
        # t.append(i["id"])
    return render_template('index.html', contacts=myData)

@app.route('/page/<id>',methods=["GET"])
def page(id):
    row=data[data['id']==int(id)].values
    print(row)
    return render_template('page.html',contacts=row)
    



if __name__ == "__main__":
    services.upload_data(data)
    app.run(debug=True)