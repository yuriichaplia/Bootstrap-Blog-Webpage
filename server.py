import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

blog_data = requests.get(url="https://api.npoint.io/85adf096d1c1ab93961b")
blog_data.raise_for_status()
blog_data = blog_data.json()

@app.route('/')
def home_page():
    return render_template('index.html', data = blog_data)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/post/<number>')
def post_page(number):
    title = blog_data[int(number) - 1]['title']
    subtitle = blog_data[int(number) - 1]['subtitle']
    date = blog_data[int(number) - 1]['date']
    body = blog_data[int(number) - 1]['body']
    return render_template('post.html',
                           title=title, subtitle=subtitle, date=date, body=body)

if __name__ == "__main__":
    app.run(debug=True)