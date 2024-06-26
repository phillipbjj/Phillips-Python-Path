"""Web address: pjdempsey3.pythonanywhere.com"""

from flask import Flask, request        #Imports and initializes my flask application
app = Flask(__name__)
                                        #Defines a route in Flask using @app.route() decorator.
@app.route('/chat', methods=['POST'])    #/chat is the endpoint that accepts POST requests.
def chat():                             #Function that returns the rponse for that route
    message = request.form["message"]   #request.form['message'] gets message from POST request.
    
    response = "Message eceived hehe :3: " + message
    return response