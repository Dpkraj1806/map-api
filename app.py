from flask import Flask,render_template,request,redirect
import requests

app=Flask(__name__)


@app.route("/")
def home():    
    return render_template("index.html")


@app.route("/output",methods=["GET","POST"])
def output():
    if request.method== "POST":
        origin=request.form['origin']
        destination=request.form['destination']
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&units=imperial&key=[API-KEY]"
        response=requests.get(url)
        originimgurl="https://app.zenserp.com/api/v2/search?apikey=7e444ee0-462d-11ed-aa22-17c327ad7cbe&q="+origin+"&tbm=isch"
        destinationimgurl="https://app.zenserp.com/api/v2/search?apikey=7e444ee0-462d-11ed-aa22-17c327ad7cbe&q="+destination+"&tbm=isch"
        originresponse=requests.get(originimgurl)
        # destinationresponse=requests.get(destinationimgurl)
        return render_template("output.html",responses=[response.json(),originresponse.json()])

if __name__ == "__main__":
    app.run(debug=True)
