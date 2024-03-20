# We need a database to work with!
# Connect to MySQL by importing through your mysqlconnection file
# If your mysqlconnection is in config it will need a file route
from flask_app.config.mysqlconnection import connectToMySQL
#use pretty print to make terminal prints easier to read
from pprint import pprint
from flask import flash

#Create a class and remember that this class will need to be imported into server.py
class Template:
    #create a variable that connects to the correct database
    DB = "templates_schema"

    #initialize!!
    def __init__(self, data):
        #EVERY COLUMN FROM OUR DATABASE MUST BE IMPORTED HERE
        #self is FOR this .py file, data is FROM the database
        #The order DOES matter
        self.id = data ['id']
        self.faux_data1 = data['faux_data1']
        self.faux_data2 = data['faux_data2']
        self.faux_data3 = data['faux_data3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#NOW that we have properly imported the data from our database, we can start running class methods

#create a class method using this:
    @classmethod
    #we need to pass this class in as an argument, as well as the data because we are sending data to the database
    def create_placeholder(cls, data):
        #assign our query to a string called query
        #This particular query is to insert data into our database
        #Include the command to insert into the table 
        #Include the locations of the insertions
        #Include the values (data) you are inserting
        #Include NOW() for NOW timestamp
        query = """INSERT INTO templates 
        (faux_data1, faux_data2, faux_data3, 
        created_at, updated_at) VALUES (%(faux_data1)s, %(faux_data2)s, %(faux_data3)s, NOW(), NOW())"""

        #connectToMySQL is a class method that is defined in the mySQLConnection class of our mysqlconnection sheet that actually connects us to our database using any argument we provide as the link to the database
        #So, return our connected database using our class and our database name
        #then using the . we access the query_db class method and provide it with our query variable and data as the arguments
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results)
        return(results)
        #Now in order for this to ~work~ this class needs to be imported into our server.py

#This part of our logic should not be read UNTIL you have imported the previous information into the server.py, created a html sheet to take in the data, and created an html sheet to display the data
#If you have not done that yet, please do that and come back after
    
    #We now create a class method that will GET ALL of our placeholders
    @classmethod 
    #There is no need to pass in data on this method because we are only selecting
    def get_all(cls):
        query = "SELECT * FROM templates"
        #This is the same logic from the previous class method
        results = connectToMySQL(cls.DB).query_db(query)
        #Create an empty string to pass all new data into
        placeholders = []
        #Create a for loop that iterates through each item in the results
        #SO, if we just submitted data from our root route, upon redirecting to the new page, we will call this function which will iterate through every item in the database
        #in this case the placeholder is arbitrary, it could be I or X if you wanted
        #append to your empty placeholders string, and placeholder that is found in the class
        for placeholder in results:
            placeholders.append(cls(placeholder))
        print(placeholders)
        return placeholders 
        #Now that this class method is complete, we can call it in our server.py file under the appropriate route
    #Now we will validate user inputs to prevent any code breaking
    @staticmethod
    def validate_template(placeholder):
        is_valid = True
        if len(placeholder['faux_data1']) < 1 :
            flash('Input must be at least 1 character')
            is_valid=False
        if len(placeholder['faux_data2']) < 1:
            flash('Input must be at least 1 character')
            is_valid=False
        try:
            faux_data3 = int(placeholder['faux_data3'])
        except ValueError:
            flash('Faux Data 3: Input must be a number')
            is_valid = False
        else:
            if faux_data3 < 1:
                flash('Faux Data 3: Input must be at least 1 character')
                is_valid = False
    
        return is_valid


