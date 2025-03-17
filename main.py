from flask import Flask

# Initialize the Flask app
app = Flask('_name_')

# Define the route for the home page
@app.route('/')
def hello_world():
    return 'Wilson es la onda'

# Run the app
app.run(debug=True)
