from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random-nonsense'


def connection():
    server = 'localhost'
    db = 'bucklistweb'
    uid = 'Sky'
    pwd = 'P@$$word'
    conn = pymysql.connect(host=server, user=uid, password=pwd, database=db)
    conn.autocommit(True)
    return conn


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        conn = connection()
        conn.close()

    return render_template("signup.html")

@app.route('/activities')
def activities():
    return render_template("activities.html")

@app.route('/destinations')
def destinations():
    destination_url = "https://www.theblondeabroad.com/ultimate-venice-travel-guide/"
    return render_template("destinations.html", destination_url=destination_url)

@app.route('/lists')
def lists():
    return render_template("lists.html")

if __name__ == "__main__":
    app.run(debug=True)
