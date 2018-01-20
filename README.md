 # Andela Accomodations

 [![Maintainability](https://api.codeclimate.com/v1/badges/7ef52ff63bae08cb40be/maintainability)](https://codeclimate.com/github/CeciliaCaroline/andela_facilities/maintainability)

 [![Coverage Status](https://coveralls.io/repos/github/CeciliaCaroline/andela_facilities/badge.svg?branch=master)](https://coveralls.io/github/CeciliaCaroline/andela_facilities?branch=master)

 [![Build Status](https://travis-ci.org/CeciliaCaroline/andela_facilities.svg?branch=master)](https://travis-ci.org/CeciliaCaroline/andela_facilities)

The Andela accomodations app is an accommodations management app. It allows users to track and manage room allocations, facilitate the clearance of fellows when moving out, track issues in Andela accommodations. 

## Requirements
The application  utilises the Django Rest Framework. The app has been tested for python 3.6 and uses the sqlite database.

## SetUp
Create a project directory

`$ mkdir Accomodations`
`cd Accommodation`

Create a virtual environment and activate it:

` virtualenv --python=python3 env `
`source env/bin/activate`

Clone this repository as shown below:

`$ git clone https://github.com/CeciliaCaroline/andela_facilities.git`

Then install the required dependencies

`pip install -r requirements.txt`


## Run

Start the development server

`python manage.py runserver`

## Testing

You can run the tests with the following command:

`python manage.py test`
