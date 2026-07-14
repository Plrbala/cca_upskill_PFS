from flask import Flask,render_template,request,flash

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    message=""
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]

        if username=="admin" and password=="12345":
            message="login successfull"
        else:
            message="Invalid UserName and Password"
    return render_template("login.html",msg=message)


if __name__=="__main__":
    app.run(host='127.0.0.1', port=5004, debug=True)