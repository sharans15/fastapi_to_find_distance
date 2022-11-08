# fastapi_to_find_distance


INTRO:This project demonstrates a FastAPI which enables the user to store the location or addrees of a place by simply enter the name of the place and the biggest change in this project
from the former one is that:
 
WE FIRST GET ALL THE FIELDS OF ALL PLACES AND THEN WE USE THE NAME FIELD OF THE PLACES AND GET THE DISTANCE OF THESE PLACES FROM THE USERS CURRENT LOCATION.
THIS WAY WE CHECK THE CONDITION AND SEE IF IT IS MATCHING THE REQUIRED CRITERIA
FOR EXAMPLE IF THE DEVELOPER ENTERS A CITY BANGALORE WHILE SITTING AT MUMBAI 
THEN THE DISTANCE SAY IS 900 MILES AND NOW THE CONSUMER IF RUNS THIS API FROM BANGALORE 
WITH A FILTER OF PLACES FARTHER THAN 800 MILESS THEN BY LOGIC BANGALORE SHOULD NOT COME WHILE THE
CONSUMER IS IN BANGALORE BECUSE BANGALORE IS NOT 900 MILES FROM BANGALORE.
SO THIS HAS BEEN APPLIED HERE.


Requirements:
1) python 3.7 or 3.8
2) sql database application (get it from "https://sqlitebrowser.org/dl/") : This will help you to see which data has gone in which table and so accordingly you can
test and run
3) open the DB browser and chose "open database" and choose the db file (named "database") which is present in "\my-projects-master\my-projects-master"


For running and Understand the flow of project:
Step 1 : clone this repository or simply download in zip file
step 2: run the command "pip install -r requirements.txt (this installs all the necessary libraries needed)
step 3: then in terminal run "uvicorn main:app --reload"
step 4: you will see this message on terminal "Application startup complete."
step 5: then on your webbrowser just open "http://localhost:8000/docs#/"

step 6: you will see the built in Swagger UI open with the following opt

        1)Gems (This contains the location detials,that is "location" and its distance)
        
            1) get method: here you can enter the filter for the seeing places farther than a particular distance (unit is in miles) and hence we have the variable name as "places_farthet than"
             And then the locations matching the criteria will show up .
             No authentication needed for this and initially i have stored a few places like mumbai delhi etc along with some test places saved with the default name 
             "string" .
               
             2) post method : here you can add places (like mumbai,delhi,bangalore,amritsar etc) and distance value will be set to 0 by default and you
             need not change that because afer you choose the city or place or address the corresponsing distance will be assigned to the respective id
             by the help of haversine library, and id is the city which you are entering. And your current location will be fetched from the library geocoder
             This needs AUTHENTICATION
             
             3)put method : Here you can update the address. So for a given id you can put any address and any latitude and longtitude as desired.
             This needs AUTHENTICATION and also the entered ID should exist.
             
             4) delete : Here you can enter the ID and delete the same.
             This needs AUTHENTICATION and also the entered ID should exist.

          2)User
          
             1) Post registration : here you can register and password should be atleast 6 characters and username should be unique and unused.
             is_auth parameter shall be true by default and not be changed.
             
             2) Post login : here you will login with correct credentials as entered during registration and then you will see a token generated and then you will click on the
             lock sign and enter the token to get authenticated.
             
             3) get users: you can see your user credentials
             This needs AUTHENTICATION.
