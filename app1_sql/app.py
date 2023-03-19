# Import necessary libraries
import mysql.connector  # MySQL connector library to interact with the MySQL database
import random  # Used for selecting a random fortune
import os  # Provides access to environment variables
from flask import Flask, render_template  # Flask web framework and render_template function for rendering HTML templates

# Initialize Flask application
app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': os.environ['db_username'],  # Get the database username from an environment variable
    'password': os.environ['db_password'],  # Get the database password from an environment variable
    'host': os.environ['container_ip'],  # Get the IP address of the container hosting the MySQL database from an environment variable
    'database': 'my_database1'  # Name of the database to connect to
}

# Define the root route ('/') for the Flask application
@app.route('/')
def index():
    # Connect to the MySQL database using the connection configuration defined above
    cnx = mysql.connector.connect(**db_config)
    
    # Create a cursor object to interact with the database
    cursor = cnx.cursor()
    
    # Execute a SQL query to fetch all fortunes from the 'fortunes' table
    cursor.execute("SELECT fortune FROM fortunes")
    
    # Fetch all the rows returned by the query and extract the first column (fortune) from each row
    fortunes = [row[0] for row in cursor.fetchall()]
    
    # Select a random fortune from the list of fortunes
    random_fortune = random.choice(fortunes)
    
    # Close the cursor and the database connection
    cursor.close()
    cnx.close()
    
    # Render the 'index.html' template and pass the random fortune to be displayed
    return render_template('index.html', fortune=random_fortune)

# Start the Flask development server if the script is run directly
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
