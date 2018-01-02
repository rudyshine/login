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
        # ##启动爬虫
        # spider_name = "e_login"
        # subprocess.check_output(['scrapy', 'crawl', spider_name, '-a' 'start_urls='+start_urls])

        return redirect(url_for('success',start_urls=request.form['start_urls']))
    else:
        return "false"

@app.route('/success')
def success():
    start_urls = request.args.get('start_urls')
    ##启动爬虫
    spider_name = "e_login"
    subprocess.check_output(['scrapy', 'crawl', spider_name, '-a' 'start_urls=' + start_urls])
    return render_template('success.html', start_urls=request.args.get('start_urls'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)
    # app.run(host='0.0.0.0', port=5555)