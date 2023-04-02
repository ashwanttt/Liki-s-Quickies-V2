from flask import Flask, render_template, jsonify

app = Flask(__name__)
NAME="Liki's"
JOB = [
    {
        "title": "Line Cook",
        "location": "New York, NY",
        "salary": "$15 - $20 per hour",
        "description": "Responsible for preparing food to order in a fast-paced restaurant kitchen."
    },
    {
        "title": "Server",
        "location": "Los Angeles, CA",
        "salary": "$10 - $15 per hour + tips",
        "description": "Provide excellent customer service and ensure all guests have a pleasant dining experience."
    },
    {
        "title": "Bartender",
        "location": "Chicago, IL",
        "salary": "$12 - $18 per hour + tips",
        "description": "Mix and serve drinks to patrons, maintain a clean bar area, and ensure guests are satisfied with their drinks."
    },
    {
        "title": "Dishwasher",
        "location": "Houston, TX",
        "salary": "$10 - $12 per hour",
        "description": "Responsible for cleaning and sanitizing dishes, utensils, and kitchen equipment."
    },
    {
        "title": "Host/Hostess",
        "location": "Miami, FL",
        "salary": "$10 - $15 per hour",
        "description": "Greet guests, manage the waitlist, and ensure all guests are seated promptly."
    },
    {
        "title": "Sous Chef",
        "location": "Seattle, WA",
        "salary": "$40,000 - $60,000 per year",
        "description": "Assist the head chef in managing the kitchen and creating new menu items."
    }
]


@app.route("/")
def hello():
        return render_template('home.html', jobs=JOB, name=NAME)

@app.route("/api/jobs")
def jobs():
      return jsonify(JOB)

if(__name__) == "__main__":
    app.run(host='0.0.0.0', debug=True)

