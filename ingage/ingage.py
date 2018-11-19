from flask import Flask, render_template, request
import instaScrape
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	userInfo = instaScrape.scrape(name)
	#comment = request.form['comment']
	print(userInfo)
	#return render_template('index.html', name=name, comment=comment)
	return render_template('index.html', name=userInfo[1])

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)