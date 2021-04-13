from flask import Flask, render_template
app = Flask(__name__)


app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/advice/")
def advice():
    return render_template('advice.html')

@app.route("/blog/")
def blog():
    return render_template('blog.html')

@app.route("/bookshelf/")
def bookshelf():
    return render_template('bookshelf.html')

@app.route("/culture/")
def culture():
    return render_template('culture.html')

@app.route("/fast/")
def fast():
    return render_template('fast.html')


@app.route("/labs/")
def labs():
    return render_template('labs.html')

@app.route("/growth/")
def growth():
    return render_template('growth.html')

@app.route("/links/")
def links():
    return render_template('links.html')

@app.route("/people/")
def people():
    return render_template('people.html')

@app.route("/pollution/")
def pollution():
    return render_template('pollution.html')

@app.route("/progress/")
def progress():
    return render_template('progress.html')

@app.route("/questions/")
def questions():
    return render_template('questions.html')

@app.route("/svhistory/")
def svhistory():
    return render_template('svhistory.html')

@app.route("/travel/")
def travel():
    return render_template('travel.html')

@app.route("/work/")
def work():
    return render_template('work.html')


if __name__ == "__main__":
    app.run()