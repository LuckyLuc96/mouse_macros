# This module will read the html of the applications page and return the location of the target job. 
# It will read the name of the jobs posted and search for the keywords the client desires
# If a keyword is detected in a job, IE: "Plumbing" it will return to the main program the location 
# Then the main file will select that job and then begin the application process

import requests

class GetTarget():
    request = requests.get('https://google.com')