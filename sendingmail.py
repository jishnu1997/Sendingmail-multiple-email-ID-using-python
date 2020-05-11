import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "from email"
col_list = ["CSV col names "]

df = pd.read_csv("data.csv", usecols=col_list)
for i in df["email col name "]:
    to = i
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Subject"
    msg['From'] = me
    msg['To'] = to

    text = " "
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi <br>
            <br>
                line1<br>
                line2<br>
           <br>
           <b>line3</b><br>
           line4
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('email', 'password')
    mail.sendmail(me, to, msg.as_string())
    mail.quit()