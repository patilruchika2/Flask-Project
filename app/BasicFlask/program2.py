from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route("/")
def index():
    name="Python Flask Workshop"
    line="i m the color of sun"
    list=[4,67,89,34,3,2,6,8,70]
    tup=("arshee","sam")
    dictt={"Name":"ruchika","Age":19,"college":"Ruia"}
    Nlist=[{"Favouritecolor":["red","yellow"]},{"favouritefood":["pizza","burger"]}]
    return render_template('tmp.html',name1=name,list1=list,tup1=tup,dictt1=dictt,line1=line,Nlist1=Nlist)#html_variable=python_variable


if __name__=="__main__":
    app.run(debug=True)

'''@app.route("/admin")
def hello_admin():
    return "Admininstator Area, guest is not allowed"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Guest User %s not having admin rights" %guest

@app.route("/user/<name>")
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest' , guest=name))'''

