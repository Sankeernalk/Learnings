import flask
import smtplib

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def send_email():

    try:

        subject = "Summary of your meeting"
        with open("/Users/sankeernalk/Desktop/git/GitFirstRepository/summary_momeric.txt") as f:
            msg = f.read()

        server = smtplib.SMTP('smtp.gmail.com:587')

        server.ehlo()

        server.starttls()

        server.login('hackathonerichack@gmail.com', 'Eric@123')

        message = 'Subject: {}\n\n{}'.format(subject, msg)

        server.sendmail('abc@gmail.com','hackathonerichack@gmail.com', message)

        server.quit()

        return "successfully sent.."

    except:
        return "failed to send message"

if __name__ == '__main__':
    app.run()