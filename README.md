*Note: I spilled water on my computer, which means that part of this project was completed on a backup computer. So the GitHub has commits from both "Sara Morell" and "Joe Klaver." However, both of those represent work done entirely by me.*

# Project Title: Campaign Advertisement Transcription Project

Sara Morell

https://github.com/smorell93/SI507_Final

---

## Project Description
This project is a Flask application that shows a campaign ad and has the user fill out information about the ad.

#### Project Purpose
This summer, I will be hiring undergraduate research assistants to transcript campaign advertisements from 2016 races for the U.S. House. This data comes from the Wesleyan Media Project, but it comes in the form of video files with coded variables, rather than written transcripts. I need these undergraduate coders to transcribe the ad and then note the gender of the candidate. I also need to be able to track how many hours they've worked and how much they are being paid.

#### What The Code Does
Each user will view a random campaign ad in a Flask application, which also provides them with a form to fill out for the new information. The new information includes both the transcript and the candidate gender. The Flask application will also show them helpful information, like the candidate's name, the district for the race, and the opponent's name (if the database has it).

My code will then save their responses in a csv file, which has a many-to-one relationship with the campaign ads. It is a many-to-one relationship, because many users can transcribe the same ad. This ensures that I can measure intercoder reliability.

Next, there will be a separate route with a form where they can fill out information about the total number of hours they have worked in a particular session and how many advertisements they transcribed in that time. When they submit that information, it will take them to a submission page that shows their total number of hours worked. The user information has a many-to-many relationship with the ad information, because users code many ads and ads are coded by many users.

## How to Run

1. First, you should install all of the requirements with pip install -r requirements.text
2. Second, you should check that you have a set of video files in a folder labeled "static." These videos are a random sample of the 600,000 ads in the dataset. These video files correspond to the wmphouse2016.csv file, which provides information about each ad.
2. Next, you should run python SI507_finalproject.py
3. You can run the tests by running SI507project_tests.py

## How to Use

1. When you run SI507_finalproject.py, it provides a link "http://127.0.0.1:5000/" to the Flask homepage. You should start by going to this link. If you have gone to the correct link, you should see a page that looks like this:

![Homepage](ss1.png)

2. Click the button that says ""

## Routes in this Application

- '/campaign_ad/input'
  - This Flask route is already completed and shows the
- '/campaign_ad/submit'
  - This route is where the data from the input route will be submitted
- '/student/hours_tracking'
  - This route will be where the users will input how many hours they've spent transcribing ads and how many ads they've transcribed in that time.

## How to run tests

- My tests are kept in the same directory as my other files. So all you need to do is run python SI507project_tests.py.

## In this Repository:

* **SI507_finalproject.py:** This file includes all of my code, including classes, functions and flask routes
* **SI507project_tools.py:** This file includes all of the classes and functions I have created for the check in.
* **SI507project_tests.py:** This file includes the tests I will use to confirm my project is working.
* **README.md:** This file is my README, with the summary of the project.
* **static/VideoFiles:** This is a folder of the 12 video files that I am using as a sample for this project. (The full database is 600,000 video files, but that was too large for GitHub to handle)
* **templates:** This is a folder of my HTML templates
* **Final_Project_Database_Diagram.pdf:** This is my database diagram, which shows the relationships between the three tables that I am creating for this project.
* **wmphouse2016.csv:** This is the csv file that I'm pulling the candidate information from. Each row in the csv file represents one instance of a campaign ad.

## Code Requirements for Grading

### General

- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working


### Flask application

- [ ] Includes at least 3 different routes
- [X] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [X] Interactions with a database that has at least 2 tables
- [X] At least 1 relationship between 2 tables in database
- [X] Information stored in the database is viewed or interacted with in some way

### Additional Components

- [X] Use of a new module: Pandas
- [ ] A many-to-many relationship in your database
- [X] At least one form in your last application
- [X] Templating in your Flask application
- [ ] Inclusion of Javascript files in the Application
- [X] Relevant use of 'itertools'


### Submission

- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
