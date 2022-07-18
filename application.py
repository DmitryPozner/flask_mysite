# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

application = Flask(__name__)

@application.route("/")
def root():
    skills = ['Linux Servers and Windows Servers','Scripts on bash, python, powershell','CI/CD (Jenkins, Github Actions)','Docker, K8s, Ansible','Git']
    contacts = [
        {
            'service' : 'GitHub',
            'link' : 'https://github.com/DmitryPozner'
        },
        {
            'service' : 'Mail', 
            'link' : 'https://yandex.mail.ru'
        }
    ]
    return render_template("index.html", title = 'Dmitry`s Web Page', skills = skills, contacts = contacts)

@application.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'root' and password == 'pass': message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port = 80)
    
