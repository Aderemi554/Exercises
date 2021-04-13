from flask import Flask, render_template
app = Flask(__name__)




# @app.route("/about/")
# def about():
#     return render_template('about.html')

@app.route("/advice/")
def advice():
    return render_template('advice.html')

# @app.route("/blog")
# def blog():
#     return render_template('blog.html')

# # @app.route("/bookshelf")
# # def bookshelf():
# #     return render_template('bookshelf.html')

@app.route("/")
def culture():
    return render_template('culture.html')

# @app.route("/fast")
# def fast():
#     return render_template('fast.html')

# @app.route("/growth")
# def bookshelf():
#     return render_template('growth.html')

if __name__ == "__main__":
    app.run(debug=True)