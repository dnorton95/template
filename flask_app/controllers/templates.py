from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.template import Template
#Create an HTTP Root Route, a homepage
@app.route("/")
#Define a function that you want to be performed when this route is opened
def index():
    #In this case, we're rendering an html template that we will build
    return render_template("template.html")

#this is the route that we defined in our HTML template
@app.post("/create")
#define a class method
def create():
    if not Template.validate_template(request.form):
        return redirect('/')
    #import the class method functionality from the correct controller, and use a . to grab the class method
    #using the class method, we'll request the form from our HTML sheet
    Template.create_placeholder(request.form)
    #never return a render_template when users are inputting info
    #return a redirect to an HTTP route that will render our HTML template
    return redirect("/all_placeholders")

#Whenever we return a redirect, we need route that it redirects to
@app.route("/all_placeholders")
def all_placeholders():
    #call the class method you defined that iterates through the entire db and returns it
    #call this class method inside of a variable so the variable can be passed as an argument
    templates_variable = Template.get_all()
    #as an argument we need to set our empty placeholders list and = templates_variable 
    return render_template("all_placeholders.html", placeholders=templates_variable)
