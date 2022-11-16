from flask import *

import sendgrid
from sendgrid.helpers.mail import *

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index'))

def send_email(name, email, message):
    my_mail = 'edmanriquer@gmail.com'
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    from_email = Email(my_mail)
    to_email = To(my_mail, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message
    })

    html_content = """
        <p>Hey! You have a new contact from the website:</p>
        <p>Name: -name-</p>
        <p>Email: -email-</p>
        <p>Message: -message-</p>
    """

    mail = Mail(my_mail, to_email, 'New contact from website', html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())






