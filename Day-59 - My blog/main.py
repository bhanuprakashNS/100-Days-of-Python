# ....................... My Blog ......................................#
# ......... Created and modified by N.S.Bhanuprakash on 21-05-2022 .... #
from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)
blog_text_url ="https://api.npoint.io/3b18a4822bae188737be"
response = requests.get(url=blog_text_url)
blog_data = response.json()
# print(blog_data)
from_email = "smtptrial22@gmail.com"
password = os.getenv("password")
print(password)
smtp_server = "smtp.gmail.com"
guy_mail_id = "nsbprakash95@hotmail.com"


@app.route("/")
def blog():
    return render_template("index.html", data=blog_data)


@app.route("/about")
def about():
    return render_template(f"about.html")


# @app.route("/contact")
# def contact():
#     return render_template(f"contact.html")


@app.route("/post/<int:num>")
def show_post(num):
    return render_template(f"post.html", data=blog_data[num-1])


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     data = request.form
#     name = data["name"]
#     mail = data["email"]
#     mobile = data["phone"]
#     msg = data["message"]
#     print(f"{name},\n{mail},\n{mobile},\n{msg}")
#
#     return "<h1>Successfully submitted!</h1>"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        method_type = request.method
        data = request.form
        name = data["name"]
        mail = data["email"]
        mobile = data["phone"]
        msg = data["message"]
        print(f"{name},\n{mail},\n{mobile},\n{msg}")

        with smtplib.SMTP(smtp_server, 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)
            connection.sendmail(from_addr=from_email,
                                to_addrs=guy_mail_id,
                                msg=f"subject:Queries from your blog!\n\n"
                                    f"name:{name}\nmail:{mail}\nmobile_number:{mobile}\nmessage:{msg}")
        return render_template(f"contact.html", post=method_type)
    else:
        return render_template(f"contact.html")


if __name__ == "__main__":
    app.run(debug=True)

