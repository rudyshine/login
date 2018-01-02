# from flask import Flask,request,render_template
# from werkzeug.utils import redirect
# from flask.helpers import url_for
# import subprocess
#
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # @app.route('/login', methods=['GET','POST'])
# # def start_login():
# #     global start_urls,username,password
# #     start_urls=request.form['start_urls']
# #     username=request.form['username']
# #     password=request.form['password']
# #     # print(username1)
# #     # return start_urls,username,password
# #     return redirect(url_for('success',username=request.form['username'],password=request.form['password'],start_urls=request.form['start_urls']))
#
# #
# @app.route('/login', methods=['GET','POST'])
# def start_login():
#     if request.method == 'POST':
#         start_urls=request.form['start_urls']
#         print(start_urls)
#         username = request.form['username']
#         password = request.form['password']
#         # print(username1)
#         # return redirect(url_for('success',username=request.form['username'],password=request.form['password'],start_urls=request.form['start_urls']))
#         success(start_urls,username,password)
#     else:
#         return "false"
#
#
# # @app.route('/success')
# def success(start_urls):
#     spider_name = "e_login"
#     subprocess.check_output(['scrapy', 'crawl', spider_name, '-a'"start_urls="+ start_urls])
#
#     # start_urls = start_login().start_urls
#     # print(start_urls)
#     # return start_urls
#     return render_template('success.html', username=request.args.get('username'),password=request.args.get('password'),start_urls=request.args.get('start_urls'))
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5554)

from flask import Flask,request,render_template
from werkzeug.utils import redirect
from flask.helpers import url_for
import subprocess

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def start_login():
    if request.method == 'POST':
        start_urls=request.form['start_urls']
        username=request.form['username']
        password=request.form['password']
        ##启动爬虫
        spider_name = "e_login"
        subprocess.check_output(['scrapy', 'crawl', spider_name, '-a' 'start_urls='+start_urls])

        return redirect(url_for('success',username=request.form['username'],
                                             password=request.form['password'],
                                             start_urls=request.form['start_urls']))
    else:
        return "false"

@app.route('/success')
def success():
    return render_template('success.html', username=request.args.get('username'),
                                              password=request.args.get('password'),
                                              start_urls=request.args.get('start_urls'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)