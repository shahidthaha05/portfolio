from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up email configuration (your existing code)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'shahidthaha4@gmail.com'
app.config['MAIL_PASSWORD'] = 'viwdskbdkpdlochd'  # Use App Password here
app.config['MAIL_DEFAULT_SENDER'] = 'shahidthaha4@gmail.com'

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_messages.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize extensions
mail = Mail(app)
db = SQLAlchemy(app)

# Define the ContactMessage model
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<ContactMessage {self.name}>'

# Create the database tables (run this in the app context)
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = [
        {"title": "Project 1", "description": "A web app for e-commerce page", "link": "https://github.com/shahidthaha05/mainpro.git"},
        {"title": "Project 2", "description": "Portfolio website using Flask", "link": "https://github.com/user/portfolio"},
    ]
    return render_template('projects.html', projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Add the form data to the database
        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()

        # Optionally, send an email notification
        msg = Message("New Message from Contact Form",
                      sender=email,
                      recipients=["shahidthaha4@gmail.com"])  # Replace with your email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        mail.send(msg)

        # Redirect to a thank you page
        return redirect(url_for("thank_you"))

@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

if __name__ == '__main__':
    app.run(debug=True)
