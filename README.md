# UOCIS322 - Project 4 #
Brevet time calculator.

## Overview

Reimplements the RUSA ACP controle time calculator with flask and ajax.

### ACP controle times

Randonneuring is a type of cycling event where riders ride a course of at least 200km (and in the US, no longer than 1200km), and they must stay within a pace window. This window is enforced with "controles," points along the course with an open time that correlates with the fastest permitted pace for the ride to that point and a closing time that correlates with the slowest permitted pace. An overview of the sport, along with some information about pacing, is available here: https://en.m.wikipedia.org/wiki/Randonneuring#Time_limits. An overview of the algorithm in the US is available here: https://rusa.org/pages/acp-brevet-control-times-calculator. The algorithm has numerous quirks, which are detailed below. The definitive source of correct times used for this project is an online controle time calculator available here: https://rusa.org/octime_acp.html.

#### Specifics of the algorithm
* Brevet distances can only be 200, 300, 400, 600, and 100km in the US.
* Pace for first 200km is between 15km/hr and 34km/hr; for 200-400km it's between 15 and 32km/hr; for 400-600km it's between 15 and 30km/hr; and for 600-1000 it's between 11.428 and 28km/hr.
* Controle distances in miles are converted to kilometers, truncated (not rounded) to the nearest integer value.
* Controle distances in km with precision more than ones are rounded to the nearest integer.
* Opening and closing times are rounded to the nearest minute.
* A controle may occur after the total brevet distance (a brevet is a course); for example, a 200km brevet may have a controle at 220km. The opening and closing times will be the same as for a controle at the brevet distance; in this case, 200km. The controle can be no more than 20% farther than the brevet distance. Thus for a 200km brevet, a controle can be at 220km, but not at 221km.
* At certain distances, the closing time is later than the calculator would yield. Thus the official closing time for a 200km brevet is 13.5 hours after the start time; for 300km it's 220 hours; for 400km it's 27 hours; for 600km it's 40 hours; and for 100km it's 75 hours after start time.
* Competitors can start within one hour of the start time. That means that a controle at 0 has a closing time one hour after the start time. 
* Due to the hour-long start window, the closing times for the first 60km are somewhat different. The minimum pace is 20km/hr, plus an additional hour added on. At 60km this formula produces the same result as the normal formula, and the normal algorithm takes over.
* Note that as the paces slow for longer brevet distances, the slower pace windows only apply to the later intervals. Thus the windows for a controle at 500km will have the 0-200km times for the first 200km, plus the 200-400km times for the next 200km, and then the 400-600 times for the remaining 100k.

## Operation instructions
### Normal operation
Download (clone) this repository.
You may wish to create your own credentials.ini file, using credentials-skel.ini as a model.
Navigate to the vocab directory. 
### To use Docker
Make sure Docker is installed on your machine (https://docs.docker.com/get-docker/)
Build a Docker image with docker build -t [name of image] . (the . is part of the command).
Run the image with docker run -d -p [your choice of port]:5000 [name of image]
Open a browser and navigate to the address of your machine and the port you've selected.
To end the program, find the process with Docker ps. Then stop the process with docker stop [process number or name]. Then if desired clear the process with docker rm [process number or name].
### To run locally without Docker
Run the program with python3 flask_vocab.py.
Open a browser on your local machine and look in localhost:5000.
To end the program, you may need to use CTRL-c.

### Testing

The script test_acp_times.py tests the open_time and close_time functions in acp_times.py, comparing the results of those functions with the online calculator mentioned above. You can run these tests from within the brevets directory by typing "nosetests" at a command line prompt; you can also move one directory up and directly run "./run_tests.sh". 

## Needed improvements / bugs

The app currently works fully to project specifications. However, it would be better with a few improvements:
* Currently if a user changes the start time or brevet distance, already-existing controle opening and closing times do not change. The app will be better if there are event handlers for changes in these values that trigger an update to the opening and closing times for all existing controle distances that a user has entered.
* Error response is very limited at this point. Input error checking (for permissable types and values) should be added to flask_brevets.py (specifically the _calc_times function) such that the results include a boolean indicator of success or failure, and if the method failed, a message indicating the reason. calc.html should be modified to display such error messages.


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
Ali Hassani updated this project and provided assistance with its implementation.
Humphrey Shi is the instructor of record.
