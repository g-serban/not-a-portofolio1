from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/helloworld') # root route, home route  #<- any time we run the server URL main page '/', we are going to get a request
def hello_world():     # with this decorater we are going to send the following function to the requester
    return 'Hello, World!'



# First we imported the Flask class. 
# An instance of this class will be our WSGI application.

# Next we create an instance of this class. 
# The first argument is the name of the application’s module or package
# you are using a single module (as in this example), 
# you should use __name__ because depending on if it’s started as application 
# or imported as module the name will be different ('__main__' versus the actual import name). 
# This is needed so that Flask knows where to look for templates, static files, and so on.
# For more information have a look at the Flask documentation.

# We then use the route() decorator to tell Flask what URL should trigger our function.

# The function is given a name which is also used to generate URLs for that particular function,
#  and returns the message we want to display in the user’s browser.

@app.route('/blog')
def blog():
    return 'Do you like blogs? I don\'t :)'

@app.route('/blog/blog')
def blog2():
    return 'I still don\'t like blogs :)'

@app.route('/dog.wow')
def dog():
   return render_template('dog.html')
if __name__ == '__main__':
   app.run()

@app.route('/users/<username>')
def hi(username=None):
    return render_template('hi.html', name=username)





