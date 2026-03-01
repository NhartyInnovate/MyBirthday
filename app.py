from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date

app = Flask(__name__,
            static_folder="static",
            template_folder="templates",
            static_url_path="/static"
            )

# ============================
# 1. WISHES DATA (EDIT THIS)
# ============================
# 👉 This is where you paste all your WhatsApp wishes.
# Copy this structure and repeat for each person.
#
# - name: who sent the wish
# - message: the wish text (you can shorten long ones)
# - relation: Friend / Family / Church / Colleague / etc. (optional)
# - timestamp: just for display (any string like "2026-02-28 09:30")
wishes = [

# ===== FAMILY =====

{
    "name": "Gloria",
    "message": """Happy happy birthday to you Big bro.

I wish you long life and prosperity, I really want to say thank you for being a big bro indeed since we were little, thank you for always having my back.

I pray that in this new age of yours, kings shall come to the brightness of your rising, whatever you set your hands to do shall prosper and favour will always follow you in Jesus name...""",
    "relation": "Family",
    "timestamp": "2026-02-28 07:12",
},

{
    "name": "Anointed",
    "message": """Happy Birthday Big Bro. 🥳🥳 Thank you for showing me what family means. I love you ❤️""",
    "relation": "Family",
    "timestamp": "2026-02-28 07:34",
},

{
    "name": "Joyce",
    "message": """Happy Birthday, my dear brother! I’m so proud of you and grateful to have you in my life. Thank you for your sacrifices and love.May this new year bring you joy, success, and all the good things you deserve. Enjoy your special day.""",
    "relation": "Family",
    "timestamp": "2026-02-28 08:01",
},

{
    "name": "Mercy",
    "message": """Happy birthday to you. May the lines fall in pleasant places for you. Amen.
May the best of the year be your portion in Jesus name. Amen 💖💖""",
    "relation": "Family",
    "timestamp": "2026-02-28 08:18",
},

{
    "name": "Mr Moses",
    "message": """Happy Birthday to you Dear. May good things keep accompanying you. live long and prosper.💞""",
    "relation": "Family",
    "timestamp": "2026-02-28 08:42",
},

{
    "name": "Popcy",
    "message": """Happy birthday. Wishing you prosperous years ahead. The Lord will connect you to a strategic destiny helper that will enable you to enter abundance of life, and  rest on all round ,and divine favour in Jesus name. AMEN.""",
    "relation": "Family",
    "timestamp": "2026-02-28 09:05",
},

{
    "name": "Mumcy",
    "message": """Happy Birthday to you my Prince.""",
    "relation": "Family",
    "timestamp": "2026-02-28 09:21",
},

# ===== FRIENDS =====

{"name":"Mrs Precious","message":"Happy birthday in arrears bro, God continues to bless and uplift you, keep thriving.","relation":"Friends","timestamp":"2026-02-28 09:45"},
{"name":"Kelvin","message":"Happy birthday man","relation":"Friends","timestamp":"2026-02-28 10:02"},
{"name":"Loveth","message":"Happy birthday Nath","relation":"Friends","timestamp":"2026-02-28 10:16"},

{"name":"Mr Emmanuel","message":"Happy birthday, good man.\nI love you.\nGod bless you over and over, granting you peace and honor 👑","relation":"Friends","timestamp":"2026-02-28 10:39"},

{"name":"King Mimshach","message":"Happy birthday Nathaniel. I bless the day I met you. You are such a a reliable and trusted person and I have loved every moment of working with you. I pray for more wisdom and grace as you enter your new year. Happy Bitthday sir !!","relation":"Friends","timestamp":"2026-02-28 11:03"},

{"name":"Mrs Jesse","message":"Happy glorious birthday to you.\nI celebrate you dearly🤗","relation":"Friends","timestamp":"2026-02-28 11:18"},

{"name":"Jerry","message":"Happy birthday Nathaniel. Long life  and prosperity to your new age 🙌","relation":"Friends","timestamp":"2026-02-28 11:37"},

{"name":"Diamond","message":"Happy birthday to my amazing friend🎉 Nathan Wishing you a day filled with love, laughter, and all your favorite things.May God bless you with joy, peace ✌️ and purpose. May your year ahead be filled with growth, love and adventure. Cheers 🥂 to another year","relation":"Friends","timestamp":"2026-02-28 12:02"},

{"name":"IZIK","message":"Happy Birthday Bro","relation":"Friends","timestamp":"2026-02-28 12:18"},

{"name":"Tessy","message":"Happy birthday my runaway husband,May your lips always wear a smile the way the sky wears the sun🙏💙","relation":"Friends","timestamp":"2026-02-28 12:32"},

{"name":"Mummy Maxson","message":"Happy Birthday!! Nathaniel,  Nations  shall call you blessed","relation":"Friends","timestamp":"2026-02-28 12:47"},

{"name":"Evelyn","message":" Long life and prosperity in good health and wealth 🌸🌸","relation":"Friends","timestamp":"2026-02-28 13:04"},

{"name":"Nathaniel","message":"Happy birthday my chairman \nYou are indeed a good person to have around your corner wishing you God’s blessings and grace \nBirthday blessings  my gee","relation":"Friends","timestamp":"2026-02-28 13:21"},

{"name":"Ibukun","message":"Happy birthday brother \nWishing you many happy returns of God's faithfulness and prosperities in perfect health","relation":"Friends","timestamp":"2026-02-28 13:40"},

{"name":"Gift","message":"Happy birthday Big Nate, I wish you the best on this day and forever. May God answer your secret prayers.","relation":"Friends","timestamp":"2026-02-28 14:03"},

{"name":"Celebration Church International","message":"Happy Birthday Nathaniel Katugwa. Your path shines brighter and brighter this year and beyond.  It’s a good year for you indeed. Thank you for all you do.","relation":"Friends","timestamp":"2026-02-28 14:26"},

{"name":"Boss Busayo","message":"Happy Birthday Nath.\nYou shall enjoy God's mercy and favor all the days of your life..\nWelcome to another level of greatness 👍👍","relation":"Friends","timestamp":"2026-02-28 14:48"},

{"name":"Faith","message":"Happy happy birthday dearest Nath. Oh, how I pray you flourish in the knowledge of God and in your accomplishment of all you desire. Keep soaring bro","relation":"Friends","timestamp":"2026-02-28 15:10"},

{"name":"Mary Ann","message":"Happy Birthday Esteemed","relation":"Friends","timestamp":"2026-02-28 15:23"},

{"name":"Miss Chinwe","message":"Happy Birthday Nath!!","relation":"Friends","timestamp":"2026-02-28 15:36"},

{"name":"Noble","message":"Happy Birthday Nath. Welcome to a beautiful year.","relation":"Friends","timestamp":"2026-02-28 15:49"},

{"name":"Winny","message":"Happy Birthday dearest Nathaniel. You're a good person. May God continue to bless you in Jesus' name.","relation":"Friends","timestamp":"2026-02-28 16:04"},

{"name":"Samuel","message":"Happy Birthday Nath 🥳🥳\nGod bless your new age and you prosper in this season","relation":"Friends","timestamp":"2026-02-28 16:18"},

{"name":"Amaka","message":"Happy birthday to you!🎂🎉continue to grow in God’s wisdom and purpose. Have an amazing day ahead!","relation":"Friends","timestamp":"2026-02-28 16:35"},

{"name":"Mr Sly Chude","message":"Happy birthday Bro . God will continue to sustain and protect you in Jesus name, Amen.","relation":"Friends","timestamp":"2026-02-28 16:52"},

{"name":"Olamide","message":"Happy birthday to you bro 🍾🎂🎂","relation":"Friends","timestamp":"2026-02-28 17:05"},

{"name":"Astrid","message":"Happy Birthday Nath. God bless you and bless your new age🤍","relation":"Friends","timestamp":"2026-02-28 17:21"},

{"name":"Leah","message":"Happy birthday 🎂🎉","relation":"Friends","timestamp":"2026-02-28 17:34"},

{"name":"Obed","message":"Happy Birthday Nathaniel 🎉🕺🎉","relation":"Friends","timestamp":"2026-02-28 17:48"},

{"name":"Ishiaku","message":"Nathaniel!! Mgl my  oz many more years many happy returns my bro.","relation":"Friends","timestamp":"2026-02-28 18:02"},

{"name":"Franka","message":"Birthday boy\n\nHappy birthday, my dearest Nathy!! Here’s to a year filled with happiness, laughter, answered prayers and good health. \nMay God’s Favour and Grace be upon. 🎂🎂🥳🥳🎉","relation":"Friends","timestamp":"2026-02-28 18:19"},

{"name":"Mrs Blessing","message":"Happy birthday dear \nHave an amazing new year ✨️","relation":"Friends","timestamp":"2026-02-28 18:33"},

{"name":"Rosemary","message":"Happy Birthday Nathaniel 🎂🥳🎂","relation":"Friends","timestamp":"2026-02-28 18:47"},

{"name":"Alice","message":"Happy Birthday Nathaniel ❤️\nMGL 💕","relation":"Friends","timestamp":"2026-02-28 19:02"},

{"name":"Debbie Uyi","message":"Happy birthday to u 🎉🎉🎉, wish u long life and prosperity ❣️","relation":"Friends","timestamp":"2026-02-28 19:16"},

{"name":"Achiever","message":"Age gracefully Man. Cheers to your new age.","relation":"Friends","timestamp":"2026-02-28 19:29"},

{"name":"Rotma","message":"Happy birthday Nathaniel 😍😚\nToday I wish you pure happiness  joy more grace \nYou will have more of 28 February and the days of your life on earth will be filled with happiness \nWhat ever you do \nYou will prosper \nIt’s shall well with you  amen 🙏 \nEnjoy your day 😊🤗 my dear friend","relation":"Friends","timestamp":"2026-02-28 19:52"},

{"name":"David Kolawole","message":"Happy Birthday Bro.\n\nThe Lord bless you, keep you, and cause his face to shine upon you and give you peace.\n\nThe Lord's favour surrounds you like a shield.\n\nIn Jesus name, Amen.","relation":"Friends","timestamp":"2026-02-28 20:10"},

{"name":"Collins","message":"Happy Birthday, Nathaniel.\nHere’s to many more beautiful trips around the sun 🥂","relation":"Friends","timestamp":"2026-02-28 20:24"},

{"name":"Rotimi","message":"Happy Birthday Bro","relation":"Friends","timestamp":"2026-02-28 20:39"},

{"name":"Mrs Adaobi","message":" Happy Birthday, Nathanial! 🎊 Wishing you a day filled with laughter, love, and all the things that make you happiest. May this year bring you endless joy, success, and unforgettable memories!","relation":"Friends","timestamp":"2026-02-28 20:57"},

{"name":"CCI Light Unit","message":"Happy birthday @Nathaniel Katugwa 🥳🥳🎂🎊🎈\n\nThank you for all that you do for the team. We celebrate you today, may all your heart desires come to fruition. God that sees your labour of love done in secret rewards you openly. Welcome to your best year yet! 🙌🏾🙌🏾","relation":"Friends","timestamp":"2026-02-28 21:15"},

{"name":"Miss Bukky","message":"Happy birthday Nathaniel,\nThank you for all you do for the light unit. I am extremely grateful. \nI pray that you do great things with ease this year.\nGod bless you and welcome to one of your best years yet!","relation":"Friends","timestamp":"2026-02-28 21:33"},

{"name":"Mandy","message":"Happy birthday Nathaniel🥂🥂","relation":"Friends","timestamp":"2026-02-28 21:47"},

{"name":"Miss Hart","message":"Happy birthday Nathaniel!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nHonestly I am the one blessed to have you in my life.\n"
                              "What a covenant brother you are!!! May this new season come with an incredible wave of the miraculous...""",
 "relation":"Friends","timestamp":"2026-02-28 22:04"},

{"name":"Blessing B.","message":"Happy birthday Nathan 🎉🎂🎂 thank you for all you do and who you are, I celebrate you and I pray that this new year is blissful and prosperous for you. God bless you richly have an amazing year ahead.","relation":"Friends","timestamp":"2026-02-28 22:18"},

{"name":"Edafe","message":"My broooooooo! Happy birthdayyyyyyyy!!","relation":"Friends","timestamp":"2026-02-28 22:26"},

{"name":"Caleb","message":"Happy Birthday! 🎉 Bro❤️💯❤️\nTrusting, caring, and good brother like you are very, very important.\nMay your day be full of joy, laughter,😂 and wonderful memories.💯Wishing you success, good health, 😊 and happiness always. Have a great year ahead!...""","relation":"Friends","timestamp":"2026-02-28 22:39"},

{"name":"Gladys","message":"Happy birthday  brother","relation":"Friends","timestamp":"2026-02-28 22:47"},

{"name":"Williams","message":"Happy birthday to you Nathaniel.","relation":"Friends","timestamp":"2026-02-28 22:53"},

{"name":"Nelson","message":"Happy Birthday to you Bro. More years in happiness,  peace, good health and prosperity ijn","relation":"Friends","timestamp":"2026-02-28 23:01"},

{"name":"Israel","message":"Happy Birthday Nathaniel","relation":"Friends","timestamp":"2026-02-28 23:07"},

{"name":"Blessing O.","message":"Ewooo 😂 my favorite person is plus one today, and I almost forgot never 😪. Happy Birthday!!!","relation":"Friends","timestamp":"2026-02-28 23:14"},

{"name":"Focus","message":"Happy Birthday bro Nath.","relation":"Friends","timestamp":"2026-02-28 23:20"},

{"name":"Jessy","message":"Happy Birthday Nath","relation":"Friends","timestamp":"2026-02-28 23:26"},

{"name":"Femi","message":"Happy birthday my Boss.... \n\nGod bless you abundantly","relation":"Friends","timestamp":"2026-02-28 23:32"},

{"name":"Director Blooms Hotel","message":"Happy birthday my Guy wishing you more of God grace and blessings with good health long life and prospects Amen","relation":"Friends","timestamp":"2026-02-28 23:38"},

{"name":"Rihann","message":"Happy Birthday Nathaniel","relation":"Friends","timestamp":"2026-02-28 23:44"},

{"name":"Confidence","message":"Happy birthday brother ♥️","relation":"Friends","timestamp":"2026-02-28 23:49"},

{"name":"Daniel","message":"Happy birthday bro🎉🎊","relation":"Friends","timestamp":"2026-02-28 23:55"},

]
# ============================
# 2. PAGE CONFIG
# ============================
BIRTHDAY_TARGET = datetime(2026, 2, 28, 0, 0, 0)


def calc_days_alive(year, month, day):
    dob = datetime(year, month, day)
    return (datetime.now() - dob).days

def calc_months_alive(year,month, day):
    dob = date(year, month, day)
    today = date.today()

    months = (today.year - dob.year) * 12 + (today.month - dob.month)

    if today.day < dob.day:
        months -= 1

    return months

def next_birthday(year, month, day):
    nxt_bd = datetime(year, month, day)
    return (nxt_bd - datetime.now()).days

def get_page_context():
    life_stats = [
        {"label": "Days Smashed", "value": calc_days_alive(1999, 2, 28)},  # change DOB if needed
        {"label": "Months Squashed", "value": calc_months_alive(1999, 2, 28)},
        {"label": "Next Birthday", "value": next_birthday(2027, 2, 28)},
        {"label": "Wishes", "value": 20},
    ]

    gallery_images = [
        {"src": "/static/img/photo1.jpg", "caption": "Grace carried me here."},
        {"src": "/static/img/photo2.jpg", "caption": "The process before the promise."},
        {"src": "/static/img/photo3.jpg", "caption": "Still learning. Still rising."},
        {"src": "/static/img/photo4.jpg", "caption": "Called. Chosen. Building."},
    ]

    target_iso = BIRTHDAY_TARGET.isoformat()
    return life_stats, gallery_images, target_iso


# ============================
# 3. ROUTES
# ============================

@app.route("/")
def index():
    life_stats, gallery_images, target_iso = get_page_context()
    confetti_flag = request.args.get("confetti", "0") == "1"

    return render_template(
        "index.html",
        wishes=wishes,
        life_stats=life_stats,
        gallery_images=gallery_images,
        target_iso=target_iso,
        confetti=confetti_flag,
    )


# You can keep this route if you still want the form to work someday.
# For now, it's optional — you don't have to use it.
@app.route("/add_wish", methods=["POST"])
def add_wish():
    name = request.form.get("name") or "Anonymous"
    message = request.form.get("message") or ""
    relation = request.form.get("relation") or ""

    if message.strip():
        wishes.append(
            {
                "name": name.strip(),
                "message": message.strip(),
                "relation": relation.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        )

    # Redirect with confetti flag so frontend knows to celebrate 🎉
    return redirect(url_for("index", confetti=1))


if __name__ == "__main__":
    app.run(debug=True)