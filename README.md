*Note: I spilled water on my computer on Monday night. So I am using a friend's backup computer to work on this project. This means that my GitHub currently says that all of the updates are coming from "Joe Klaver." This is because that's the name of the person who owns the computer. However, all of the work on this project is my own.*

##Project Description##
This project is a Flask application that shows a campaign ad and has the user fill out information about the ad.

####Project Purpose####
This summer, I will be hiring undergraduate research assistants to transcript campaign advertisements from 2016 races for the U.S. House. This data comes from the Wesleyan Media Project, but it comes in the form of video files with coded variables. I need these undergraduate coders to transcribe the ad and then note the gender of the candidate.

###What The Code Does####
They will view a random campaign ad in a Flask application, which also provides them with a form to fill out for the new information. The new information includes both the transcript and the candidate gender. The Flask application will also show them helpful information, like the candidate's name, the district for the race, and the opponent's name (if the database has it).

My code will then save their responses in a csv file, which has a one-to-one relationship with the campaign ads.

Next, there will be a separate route with a form where they can fill out information about the total number of hours they have worked in a particular session and how many advertisements they transcribed in that time. When they submit that information, it will take them to a submission page that shows their total number of hours worked.

##Summary of Files##
My Github includes the following files:

* **SI507_finalproject.py:** This file includes all of my code, including classes, functions and flask routes
* **SI507project_tools.py:** This file includes all of the classes and functions I have created for the check in.
* **SI507project_tests.py:** This file includes the tests I will use to confirm my project is working.
* **README.md:** This file is my README, with the summary of the project.
* **static/VideoFiles:** This is a folder of the 12 video files that I am using as a sample for this project. (The full database is 600,000 video files, but that was too large for GitHub to handle)
* **templates:** This is a folder of my HTML templates
* **Final_Project_Database_Diagram.pdf:** This is my database diagram, which shows the relationships between the three tables that I am creating for this project.
* **wmphouse2016.csv:** This is the csv file that I'm pulling the candidate information from. Each row in the csv file represents one instance of a campaign ad.

##Current Progress##

Thus far, I have created the classes for the campaign advertisement information and the new data that will be inputed by the user. I have also created a function that pulls a random campaign advertisement.

I have also created the flask route that displays the video file, the helpful information about the ad for the user, and an HTML form for the user to fill out. This was the bulk of my work so far, as I used an HTML template to make this work and I had some difficulty with getting a video file to play in Flask.

##What's Next##
My first next step is to save the information from the form into a CSV file.

Then I need to create the student information class, which will be the final table in my database diagram. I will need to update my two current classes (*Advertisement*, and *NewInfo*) to include their relationships with the student data.

The final step will be to create a Flask route where the student can log their hours and the Flask route that will display the information about how many hours the students have worked and how many advertisements they have transcribed.
