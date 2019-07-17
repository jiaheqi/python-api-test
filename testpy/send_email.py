import send_email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail( mail_to, sub, content):
    msg = MIMEText(content, _subtype='html', _charset="utf-8")

    main_msg = MIMEMultipart()
    main_msg.attach(msg)
    smtp_server = "smtp.163.com"
    smtp_port = "25"
    mail_user = "17600116844@163.com"
    mail_pass = "Jhq719597"
    main_msg['Subject'] = sub
    main_msg['From'] = "17600116844@163.com"
    main_msg['To'] = mail_to
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)
        server.login(mail_user, mail_pass)

        server.sendmail(mail_user, mail_to.split(';'), main_msg.as_string())
        server.quit()
        return True
    except Exception, e:
        print str(e)
        return False


def main():
    send_mail('1097099589@qq.com;13122181770@163.com','hhhh','test email')


if __name__ == '__main__':
    main()