import pymssql

class Database:
    __connection = None

    @classmethod
    def connect(cls): 
        """
        This method initializes the database connection
        """
        if cls.__connection is None:
            cls.__connection = pymssql.connect(server='cisdbss.pcc.edu', user='275student', password='275student', database='NAMES')

    @classmethod
    def readNames(cls, name, gender):
        """
        This method connects to the database and retrieves
        the top 20 names for a given year and gender
        """
        cls.connect() # Connect to database
        
        cursor = cls.__connection.cursor() # Create a custor object to execute SQL queries
        
        query = "SELECT TOP 20 Name, Year, NameCount, Gender FROM all_data WHERE Name = %s AND Gender = %s ORDER BY \"NameCount\" DESC;" 
        # Define the SQL query to retrieve top 20 names along with year, name count, and gender, all
        # specified by the user. Orders the data by NameCount in descending order. the \"NameCount\" was the only way I could get
        # the ORDER BY to function within this code. Attempted ORDER BY NameCount, ["Namecount"], and the current 
        # version which finally allowed me to retrieve data in the desired format

        cursor.execute(query, (name, gender)) # Execute SQL query with provided parameters
        
        data = cursor.fetchall() # Fetch all results from executed query
        
        return data # return fetched data from the query
