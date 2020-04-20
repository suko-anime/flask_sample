from flask import Flask, request, render_template
import unko

app = Flask(__name__)

user_name = "オチャイ"
 
@app.route("/auth", methods = ["POST"])
def login():
    user_name = request.form["userName"]
    user_password = request.form["userPswd"]
    print(unko.db_access())
    if user_name == "hogehoge" and user_password == "password":
        return render_template("hyouji.html", username = user_name)
    else:
        return render_template("index.html")

@app.route("/index.html")
def test():
    return render_template("index.html", username = user_name)

if __name__ == "__main__":
    app.run(debug=True)
