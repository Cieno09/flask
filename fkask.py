from flask import Flask,render_template

app=Flask(__name__) #create a flask object


@app.route('/')
def home():
    return('Hello World my 1st flask')

@app.route("/second")
def second():
    return ("so far this is my 2nd page")

@app.route("/selling")
def sales():
    return ("we buy low and sell high")

@app.route("/landing")  
def landing():
    return render_template("login.html")

@app.route("/land")  
def land():
    return render_template("reg.html")
    
if __name__ == "__main__":
    app.run(debug=True)

