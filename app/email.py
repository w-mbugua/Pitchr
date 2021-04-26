from flask_mail import Message
from flask import render_template
from app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def mail_message(subject,template,to,**kwargs):
    sender_email ="itsjoymbugua@gmail.com"
    msg = Message(subject, sender=sender_email, recipients=[to])
    msg.body= render_template(template + ".txt",**kwargs)
    msg.html = render_template(template + ".html",**kwargs)
    mail.send(msg)