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
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&units=imperial&key="
        response=requests.get(url)
        return render_template("output.html",responses=response.json())

if __name__ == "__main__":
    app.run(debug=True)
