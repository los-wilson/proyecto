from flask import Flask

# Initialize the Flask app
app = Flask('_name_')

# Define the route for the home page
@app.route('/')
def hello_world():
    return '<h1>Wilson es la onda<h1>'
            '<img src="https://www.muyinteresante.com/wp-content/uploads/sites/5/2022/10/13/6347f72b104ac.jpeg">'

# Run the app
app.run(debug=True)
