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

1. First, you should install all of the requirements with "pip install -r requirements.text."
2. Second, you should check that you have a set of video files in a folder labeled "static." These videos are a random sample of the 600,000 ads in the dataset. These video files correspond to the wmphouse2016.csv file, which provides information about each ad.
2. Next, you should run python SI507_finalproject.py
3. You can run the tests by running SI507project_tests.py

## How to Use

1. When you run SI507_finalproject.py, it provides a link "http://127.0.0.1:5000/" to the Flask homepage. You should start by going to this link. If you have gone to the correct link, you should see a page that looks like this: https://www.dropbox.com/s/m2rci8adg55sood/SS1.png?dl=0.

2. Click the button that says "Input Ads"

3. This button should take you to the advertisement input page. This page includes an ad for the user to view, along with a form to fill out. The user is supposed to input the ad's transcript and the candidate's gender, which are both variables I need for my research. They also put in their name, so that I can know who transcribed each ad. Each of these values is a string, and so you can put any string into the three boxes.

However, you are supposed to put the transcript of the ad in the "Transcript" box. You are supposed to put "Male," "Female," "Other/Non-Binary," or "Unsure" into the "Gender box." And you should put just your first name into the name box.

This page should look like this: https://www.dropbox.com/s/md1k4xh2d6zolg3/SS2.png?dl=0

4. Once you finish filling out the form, click the button that says "Submit" on the bottom. If this works correctly, you should see the phrase "Thanks for your submission!" appear.

5. Submitting the ad data takes you to a page that summarizes your submission. This page looks like this: https://www.dropbox.com/s/nio3m3zp6txqnpf/SS3.png?dl=0

6. On this page, you can either click "Input More Ads," which should take you back to the homepage, or you can click on "Track Your Hours," which takes the user to a form where they can track their hours working on this transcription project.

7. If the user clicks "Track Your Hours," they should come to a page that looks like this: https://www.dropbox.com/s/upq0et53es0yblk/SS4.png?dl=0.

8. On the hours tracking page, the user can fill out information about the work they've done. You must input the same name on this page as you did on the transcription page. This way the associations between the tables work.

The "Hours Worked" and "Ads Transcribed" boxes both require you to input integers. The "Questions Remaining" takes any string, and is a space for the user to tell me any issues they had when transcribing the ads.

You should then click the "Submit" button on the bottom of the page.

9. If the submit button worked, a box that says "Thanks for your submission!" should appear. You will then be taken to the final page of the Flask application, which provides a summary of the submitted information. It also includes a button that takes you back to the homepage, if you would like to keep transcribing ads.

This final page looks like this: https://www.dropbox.com/s/yl3kpjpt70jzd1i/SS5.png?dl=0

## Routes in this Application

- '/'
  - This route introduces the project and includes a button to the "/campaign_ad/input" page.
- '/campaign_ad/input'
  - This Flask route shows the ad to be transcribed and has a form where the user can fill out the candidate gender and ad transcript, as well as their name.
- '/campaign_ad/submit/<id>'
  - This route is where the data from the input route will be submitted. It provides links to submit more ads or for the user to track their hours.
- '/user_info/input'
  - This route will be where the users will input how many hours they've spent transcribing ads and how many ads they've transcribed in that time. They can also leave questions they have for me.
- '/user_info/submit'
  - This route will show the submission from the "/user_info/input" page and also provides a link to go back to the homepage.

## How to run tests

- The tests file imports from *SI507project_tools.py* and so that file must be downloaded for the tests to run.
- All you need to do is run *python SI507project_tests.py*.

## In this Repository:


* **static/VideoFiles:** This is a folder of the 12 video files that I am using as a sample for this project. (The full database is 600,000 video files, but that was too large for GitHub to handle).
  - *HOUSE_AK01_LINDBECK_BOB_HOOYMAN.mp4*
  - *HOUSE_AK01_LINDBECK_DCCC_IT'S_JUST_TIME.mp4*
  - *HOUSE_AL01_BYRNE_100_PERCENT.mp4*
  - *HOUSE_AL01_BYRNE_DANGEROUS_TIMES.mp4*
  - *HOUSE_AR02_HILL_NOT_MY_DAD.mp4*
  - *HOUSE_AR02_HILL_OLD_BLUE.mp4*
  - *HOUSE_AZ02_HEINZ_BOBBIE_THAYER.mp4*
  - *HOUSE_AZ02_HEINZ_DIFFERENT_THAN_THE_REST.mp4*
  - *HOUSE_AZ02_MCSALLY_AIR_WAR.mp4*
  - *HOUSE_AZ02_MCSALLY_MY_DAD_60.mp4*
  - *HOUSE_AZ05_JONES_LOBBYIST_GIFTS_15.mp4*
  - *HOUSE_AZ05_JONES_LYING.mp4*
* **templates:** This is a folder of my HTML templates
  - *greetuser.html:* This is the html template for the homepage ("/")
  - *userinput.html:* This is the html template for ("/campaign_ad/input")
  - *submission.html:* This is the html template for ("/campaign_ad/submit")
  - *hoursworked.html:* This is the html template for ("user_info/input")
  - *userhours.html:* This is the html template for ("user_input/submit")
* **Final_Project_Database_Diagram.pdf:** This is my database diagram, which shows the relationships between the three tables that I am creating for this project.
* **README.md:** This file is my README, with the summary of the project.
* **SI507_finalproject.py:** This file includes all of my code, including classes, functions and flask routes.
* **SI507project_tests.py:** This file includes the tests I will use to confirm my project is working.
* **SI507project_tools.py:** This file includes all of the classes and functions I have created for the check in.
* **ads_database.db:** This is an example of what the sql database could look like after the Flask app has been used repeatedly.
* **requirements.txt:** This is my requirements.txt file, which should also the programs that need to be downloaded for the program to run.
* **wmphouse2016.csv:** This is the csv file that I'm pulling the candidate information from. Each row in the csv file represents one instance of a campaign ad.


---
## Code Requirements for Grading
Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module (numpy, pandas)
- [x] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [x] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [x] Relevant use of `itertools` and/or `collections`

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
