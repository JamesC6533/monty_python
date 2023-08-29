from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random-nonsense'

items = []
users = []

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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        items = []
        for i in range(1, 16):
            item = request.form.get(f'item{i}')
            if item:
                items.append(item)
        
        return render_template('list.html', items=items)
    
    return render_template('list.html')



@app.route('/lists')
def lists():
    return render_template("lists.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
            


@app.route('/signin', methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')

    user = next((user for user in users if user['email'] == email), None)
    if user and user['password'] == password:
        return "Sign in successful!"
    else:
        return "Invalid email or password."
           

if __name__ == "__main__":
    app.run(debug=True)
