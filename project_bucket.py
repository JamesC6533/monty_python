from flask import *
import pymysql
from flask import url_for

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


@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form ["username"]
        password = request.form ["password"]
        email = request.form ["email"]
        
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("insert into customers(full_name, email, password)values('"+username+"','"+email+"', '"+password+"') ")
        return "You've succefully signed up!"
    
    return render_template("signup.html")




@app.route('/customers')
def main():
    customers = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * from customer")
    for row in cursor.fetchall():
        customers.append({"customer_id": row[0], "first_name": row[2], "last_name": row[3], "email": row[4]})
    conn.close()
    return render_template('customer.html', customers=customers)






if __name__ == "__main__":
    app.run()