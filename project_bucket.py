from flask import Flask, render_template, session, redirect, url_for, request 
import pymysql
from flask_bcrypt import Bcrypt
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

# home page 
@app.route('/')
def home():
    if 'loggedin' in session and session['loggedin'] == True:
        account_name = 'username'
    else:
        account_name = 'Login'
    return render_template("home.html", login=url_for('login'), Acount= account_name)

# user page 

@app.route('/users')
def users():

    if 'username' in session and session['logged_in']:

        username = session['username']

        conn = connection()

        cursor = conn.cursor()

        cursor.execute('SELECT * FROM customers WHERE email = %s', (username))

        customers = cursor.fetchone()

        if customers:
            return render_template('users.html', customers=customers)

    return render_template('users.html', login=url_for('login'), Acount= 'My Acount')

# sign up page
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        conn = connection()
        query = conn.cursor()

        # Hash the password
        bcrypt = Bcrypt(app)
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Use parameterized query to avoid SQL injection
        query.execute("INSERT INTO customers(username, password, email) VALUES (%s, %s, %s)",
                      (username, hashed_password, email))

        conn.close()

    return render_template("signup.html", login=url_for('login'), Acount='Sign up')

# activities page/hyperlinks
@app.route('/activities')
def activities():
    activities_url = "https://www.rivieratravel.co.uk/blog/7-wonders-the-world-explore"
    activities_url2 = "https://chillisauce.com/stag/blog/post-82d1770e6050108dddb1"
    activities_url3 = "https://www.aworldtotravel.com/best-places-to-kayak-around-the-world/"
    activities_url4 = "https://www.headout.com/blog/best-natural-wonders-of-the-world/"
    activities_url5 = "https://greenglobaltravel.com/best-cultural-festivals-around-the-world/"
    activities_url6 = "https://www.tripstodiscover.com/22-of-the-best-paddleboarding-spots-around-the-world/"
    activities_url7 = "https://brookeinboots.com/23-best-hiking-blogs/"
    activities_url8 = "https://www.planetware.com/world/best-places-to-go-snorkeling-in-the-world-us-fl-388.htm"
    activities_url9 = "https://traveltriangle.com/blog/michelin-rated-restaurants-around-the-world/"
    activities_url10 = "https://www.travelandleisure.com/best-scuba-diving-in-the-world-6944820"
    activities_url11 = "https://57hours.com/best-of/rock-climbing-worldwide/"
    activities_url12= "https://traveltriangle.com/blog/best-bungee-jumping-spots-in-the-world/"
    activities_url13 = "https://www.go2africa.com/african-travel-blog/the-road-less-travelled-africas-most-unique-safaris"
    activities_url14 = "https://www.oysterworldwide.com/news/best-places-to-ski-in-the-world/"
    activities_url15 = "https://www.touristsecrets.com/travel-guide/best-caves-in-the-world/"
    return render_template("activities.html", activities_url=activities_url,
                            activities_url2=activities_url2, activities_url3=activities_url3,
                            activities_url4=activities_url4, activities_url5=activities_url5,
                            activities_url6=activities_url6, activities_url7=activities_url7,
                            activities_ur8=activities_url8, activities_url9=activities_url9,
                            activities_url10=activities_url10, activities_url11=activities_url11,
                            activities_url12=activities_url12, activities_url13=activities_url13,
                            activities_url14=activities_url14, activities_url15=activities_url15,)

# destinations page/hyperlinks 
@app.route('/destinations')
def destinations():
    destination_url = "https://www.theblondeabroad.com/ultimate-venice-travel-guide/"
    destination_url2 = "https://www.saltinourhair.com/bali/"
    destination_url3 = "https://www.ontheluce.com/one-day-in-reykjavik/"
    destination_url4 = "https://thatadventurer.co.uk/how-to-spend-4-days-in-beijing-china/"
    destination_url5 = "https://americanandthebrit.com/3-day-guide-to-agra/"
    destination_url6 = "https://www.dreambigtravelfarblog.com/blog/places-to-visit-in-ontario-canada"
    destination_url7 = "https://www.theblondeabroad.com/ultimate-tokyo-travel-guide/"
    destination_url8 = "https://www.theblondeabroad.com/ultimate-itinerary-for-a-new-zealand-road-trip/"
    destination_url9 = "https://www.dreambigtravelfarblog.com/blog/palawan-itinerary"
    destination_url10 = "https://handluggageonly.co.uk/2017/12/07/14-beautiful-places-see-arizona/"
    destination_url11 = "https://www.saltinourhair.com/costa-rica/manuel-antonio/"
    destination_url12 = "https://www.saltinourhair.com/portugal/algarve/"
    destination_url13 = "https://maketimetoseetheworld.com/3-days-in-paris-what-to-do-itinerary-travel-tips/"
    destination_url14= "https://www.nomadicmatt.com/travel-blogs/three-days-in-amsterdam/"
    destination_url15 = "https://gretastravels.com/things-to-do-koh-phi-phi/"
    
    return render_template("destinations.html", destination_url=destination_url,
                            destination_url2=destination_url2, destination_url3=destination_url3,
                            destination_url4=destination_url4, destination_url5=destination_url5,
                            destination_url6=destination_url6, destination_url7=destination_url7,
                            destination_url8=destination_url8, destination_url9=destination_url9,
                            destination_url10=destination_url10, destination_url11=destination_url11,
                            destination_url12=destination_url12, destination_url13=destination_url13,
                            destination_url14=destination_url14, destination_url15=destination_url15)

# lists page/bucketspinner and customer lists
@app.route('/lists', methods=['GET', 'POST'])
def bucketlist():
    if request.method == 'POST':
        conn = connection()
        query = conn.cursor()
        items = []
    
        for i in range(1, 11):
            item = request.form.get(f'item{i}')
            query.execute("INSERT INTO bucketlistentries(activity) VALUES ('"+item+"') " )
            if item:
                items.append(item)
        
        return render_template('lists.html', items=items)
    
    return render_template('lists.html')

# contact page/mailing list 
@app.route('/contact')
def contact():
    return render_template("contact.html")
            

# sign up page/ sign in function 
@app.route('/signin', methods=['GET','POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')
    customerid = request.form.get('customerid')
    conn = connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE email = %s', (email))
    customers = cursor.fetchone()

    # Hash the password
    bcrypt = Bcrypt(app)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = connection()
    query = conn.cursor()

    # Use parameterized query to avoid SQL injection
    query.execute("SELECT * FROM customers WHERE email = %s", (email))
    row = query.fetchall()

    if len(row) > 0:
        # Insert hashed password into signin table
        query.execute("INSERT INTO signin(password, email, customerid) VALUES (%s, %s, %s)", (hashed_password, email, customerid))
        conn.commit()  # Commit the changes
        conn.close()

        if customers:
            password = customers[3]
            session['logged_in'] = True
            session['username'] = email
            return render_template("home.html", login=url_for('users'), Acount='My Acount', Welcome='username' )
    


    return render_template("signup.html", login=url_for('sign_up'), Acount='Sign In' )


@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form['username']
      password_candidate = request.form['password']
      conn = connection()
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM customers WHERE username = %s', (username,))
      users = cursor.fetchone()
      session ['logged_in'] = True 
      session ['username'] = username
      return render_template("home.html",login=url_for('users'), Acount='My Account')
   return render_template("signup.html",login=url_for('sign_up'), Acount='Sign up')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("home.html",login=url_for('home'), Acount='Sign In')


        
    
           
if __name__ == "__main__":
    app.run(debug=True)
