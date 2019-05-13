from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_agent = request.headers.get('User-Agent')

    if user_agent == "NCSA_Mosaic/2.0 (Windows 3.1)":
        flag = "HSCTF{wow_you_are_agent_keith_now}"
    else:
        flag = "Access Denied"

    return render_template("home.html", flag=flag, user_agent=user_agent)

if __name__ == "__main__":
    app.run()
