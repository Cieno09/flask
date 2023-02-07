from flask import Flask,render_template,request
from read_rite import account 
app=Flask(__name__) #create a flask object


@app.route('/g')
def home():
    return('Hello')


@app.route("/")  
def landing():
    return render_template("link.html")    

@app.route("/admin")
def admin():
    return ("<h1> WELCOME TO THE ADMIN PANEL</h1>")

@app.route("/new-admin")
def new_admin():
    pass

@app.route("/home")  
def welcome():
    
    user=str(request.args.get("uname"))
    password=str(request.args.get("psw"))
    b= user
    i= account(user,password)
    print(i)
    acb=(i[0])
    bnkty=(i[1])
    accnum=(i[2])

    return render_template("welcome.html",**locals())  



if __name__ == "__main__":
    app.run(debug=True)