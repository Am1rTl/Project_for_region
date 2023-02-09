from flask import Flask, abort, redirect, url_for
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        em = request.form["email"]
        passwd = request.form["passwd"]
        print(em,passwd)
        if em != '' and passwd != '' :
            return redirect(url_for('q1'), 301)
        else:
            return render_template('home.html')
    else:
        return render_template('home.html')
        
@app.route("/q1", methods=["GET", "POST"])
def q1():
    return render_template('home.html')
   
   
   
   
if __name__ == '__main__':
   app.run()
