from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message 

app = Flask(__name__)


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
    return render_template("contact.html")  # This is the contact page with the form

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Print the form data (for debugging)
        print(f"Received message from {name} ({email}): {message}")
        
        # Optionally, send an email notification
        msg = Message("New Message from Contact Form",
                      sender=email,
                      recipients=["shahidthaha4@gmail.com"])  # Replace with your email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        mail.send(msg)

        # Redirect to a thank you page (optional) or back to the contact page
        return redirect(url_for("thank_you"))

@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")  # A page to show after the form submission


    

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'shahidthaha4@gmail.com'
app.config['MAIL_PASSWORD'] = 'viwdskbdkpdlochd'  # Use App Password here
app.config['MAIL_DEFAULT_SENDER'] = 'shahidthaha4@gmail.com'

mail = Mail(app)

@app.route('/send_email')
def send_email():
    msg = Message('Hello from Flask!',
                  recipients=['recipient@example.com'])
    msg.body = 'This is a test message.'
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)