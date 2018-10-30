from flask import Flask
app=Flask(__name__)#app is variable ,__name__ is the current module
@app.route("/")#creating url,app is decorater
def index():
    return"Hello world"

@app.route("/hi/<name>")
def hello_name(name):
    return "Hello %s" %name

@app.route("/numb/<float:num>")#EXPLICITLY DEFINE THE DATA TYPE
def hello_name1(num):
    return "Hello %d" %num

#to run on browser
if __name__=="__main__":
    app.run(debug=True)
