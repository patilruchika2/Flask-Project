from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route("/")
def index():
    user={"username":"ruchika"}
    posts=[{"author":{"username":"arshee"},"body":'Beautiful day'},{"author":{"username":"maithili"},"body":'great movie'}]
    return render_template('tmp1.html',user=user,posts=posts)#html_variable=python_variable
if __name__=="__main__":
    app.run(debug=True)
