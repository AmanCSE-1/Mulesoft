import sqlite3

class Solution:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        print("Successfully connected to SQLite Database")
        
    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('DROP TABLE movies')
        cursor.execute('''CREATE TABLE IF NOT EXISTS `movies`(
                          `movie_name` text NOT NULL,
                          `lead_actor_name` text NOT NULL,
                          `lead_actress_name` text NOT NULL,
                          `release_year` int NOT NULL,
                          `director_name` text NOT NULL,
                          PRIMARY KEY (`movie_name`)
                        )''')
        cursor.close()
        self.connection.commit()
        print("Movie Table created successfully")
        
    def insert_records(self, movie_data):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO `movies` (movie_name, lead_actor_name, lead_actress_name, release_year, director_name) 
                          VALUES (?, ?, ?, ?, ?)''', (movie_data[0], movie_data[1], movie_data[2], movie_data[3],movie_data[4]))
        cursor.close()
        self.connection.commit()
        print("Record inserted into movie table succesfully")
        
    def display_all_movies(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM `movies`')
        
        result = cursor.fetchall()
        print("The Movies in the database are :")
        for row in result:
            print(row)
            
    def display_movies_with_actor(self, parameter, paramter_name):
        cursor = self.connection.cursor()
        if parameter == 'lead_actor_name':
            cursor.execute('SELECT * FROM movies WHERE lead_actor_name = ?', (paramter_name,))
        elif parameter == 'lead_actress_name':
            cursor.execute('SELECT * FROM movies WHERE lead_actress_name = ?', (paramter_name,))
        elif parameter == 'movie_name':
            cursor.execute('SELECT * FROM movies WHERE movie_name = ?', (paramter_name,))
        elif parameter == 'director_name':
            cursor.execute('SELECT * FROM movies WHERE director_name = ?', (paramter_name,))
            
        result = cursor.fetchall()
        print(f"Movies with {parameter} as {paramter_name} are :")
        for row in result:
            print(row[0])
    
    def close_connection(self, connection):
        connection.close()

object = Solution(r"Movie_Database.db")

object.create_table()
movie_data = ['Sooryavanshi', 'Akshay Kumar', 'Katrina Kaif', 2021, 'Rohit Shetty']
object.insert_records(movie_data)

movie_data = ['Bell Bottom', 'Akshay Kumar', 'Vaani Kapoor', 2021, 'Ranjit Tiwari']
object.insert_records(movie_data)

movie_data = ['Jai Bhim', 'Suriya', 'Lijomol Jose', 2021, 'T. J. Gnanavel']
object.insert_records(movie_data)

movie_data = ['Kesari', 'Akshay Kumar', 'Parineeti Chopra', 2019, 'Anurag Singh']
object.insert_records(movie_data)

movie_data = ['Zero', 'Shah Rukh Khan', 'Katrina Kaif', 2018, 'Aanand Rai']
object.insert_records(movie_data)

movie_data = ['Dangal', 'Aamir Khan', 'Sanya Malhotra', 2016, 'Nitesh Tiwari']
object.insert_records(movie_data)

object.display_all_movies()

object.display_movies_with_actor('lead_actor_name', 'Akshay Kumar')

object.display_movies_with_actor('lead_actress_name', 'Katrina Kaif')