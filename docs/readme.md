# Workout Planner
### Academic Paper: [https://drive.google.com/file/d/1m3Qux7Yl-q0rHHuQJYrFCnRMjoaYAp-V/view?usp=sharing]

We created the Workout Planner to make it easier to achieve your fitness goals. The Workout Planner allows you to 
create custom workout plans and schedules, track your progress, and display it all in a way that is easy to navigate 
and understand.


## Features

- **User Accounts**: Secure login and signups with password recovery.
- **Personalized Schedules**: Users can input data on their workout goals, experience level and current schedule for the week to generate tailored schedules.
- **Progress Tracking**: Ability to track progress over time with simple charts and graphs.
- **Schedule Management**: Ability to update schedule and change user data.
- **Profile Customization**: Ability to update goals, body measurements, and preferences from your profile.


## Setup
-Follow these steps to set up the Workout Planner

### Download Python

- **Python 3.8**: This is so you can run python and also have access to pip which is pythons package installer

### Download IDE

- **PyCharm**: We recommend installing PyCharm as it is what we used to develop the app but any IDE should work

### Setup

1. Clone the repository into your working directory:

   - git clone https://github.com/yourusername/repository

2. Install Libraries Locally

   - `Flask` - handles http requests, integrates database, provides development server
   - `Werkzeug` - handles password hashing
   - `sqlite3` - handles database
   - `re` - used for validating email
   - `pandas`, `matplotlib`, `seaborn` - for workout progress visualizations
   - `sendgrid` - used for forgot password functionality

3. Initialize the database:
   - flask initdb

4. Start the Flask development server:
   - flask run

5. Click the link generated in the terminal:
   - http://127.0.0.1:5000

## Authors

- Logan Tierney, Karsten Nordlie, Otabek Tajiev, Jacob Flores, Jimmy Marre
