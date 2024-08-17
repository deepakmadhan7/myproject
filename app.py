from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        # Implement search functionality here if needed
        return render_template('index.html', search_query=search_query)
    return render_template('index.html', search_query=None)

if _name_ == '_main_':
    app.run(debug=True)
