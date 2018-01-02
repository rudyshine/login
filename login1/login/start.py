
from flask import Flask,request,render_template
from werkzeug.utils import redirect
from flask.helpers import url_for
import subprocess

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print(request.form['start_urls'])
        print(request.form['username'])
        print(request.form['password'])
        # print(username1)
        return redirect(url_for('success',username=request.form['username'],password=request.form['password'],start_urls=request.form['start_urls']))
    else:
        return "false"

@app.route('/success')
def success():
    spider_name = "e_login"
    subprocess.check_output(['scrapy', 'crawl', spider_name])
    # with open("output.json") as items_file:
    #     return items_file.read()
    return render_template('success.html', username=request.args.get('username'),password=request.args.get('password'),start_urls=request.args.get('start_urls'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5554)


# import subprocess
#
# def start():
#     spider_name = "e_login"
#     subprocess.check_output(['scrapy', 'crawl', spider_name])
#     # with open("output.json") as items_file:
#     #     return items_file.read()
#     return "done"