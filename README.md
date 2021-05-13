# UOCIS322 - Project 4 #
Brevet time calculator.

## Overview

Reimplements the RUSA ACP controle time calculator with flask and ajax.

### ACP controle times

controle distances more than 20% over the brevet distance are not allowed
controle distances in miles are converted to kilometers, truncated to the nearest integer
controle distances in kilometers with precision more than ones are rounded to the nearest integer


That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly.  

We are essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data.  

## Getting started

In a nutshell, you will:

* Implement the logic in `acp_times.py` based on the algorithm linked above.

* Edit the template and Flask app so that the required remaining arugments are passed along.

* Create test cases using the website, and write test suites for your project.

* Update this file (`README`).

### AJAX and Flask reimplementation

The implementation that you will do will fill in times as the input fields are filled using AJAX and Flask. Currently the miles to kilometers (and some other basic stuff) is implemented with AJAX. The remainder is left to you.

### Testing

A suite of nose test cases is a requirement of this project. Design the test cases based on an interpretation of rules here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Be sure to test your test cases: You can use the current brevet time calculator [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html) to check that your expected test outputs are correct. While checking these values once is a manual operation, re-running your test cases should be automated in the usual manner as a Nose test suite.

To make automated testing more practical, your open and close time calculations should be in a separate module. Because I want to be able to use my test suite as well as yours, I will require that module be named `acp_times.py` and contain the two functions I have included in the skeleton code (though revised, of course, to return correct results).

We should be able to run your test suite by changing to the `brevets` directory and typing `nosetests`. All tests should pass. You should have at least 5 test cases, and more importantly, your test cases should be chosen to distinguish between an implementation that correctly interprets the ACP rules and one that does not.

### Replacing `README`

This `README` is currently written primarily as instructions to CIS 322 students. Replace it with a proper `README` for an ACP time calculator. Think about what should be included for users and for developers.

## Tasks

The code under `brevets` can serve as a starting point. It illustrates a very simple AJAX transaction between the Flask server and JavaScript on the web page. Presently, the server does not calculate times (just returns the current time). Other things may be missing; add them as needed. As always, you should fork and then clone this repository, make your changes, and test on the specified server at least once before you submit.

As always you'll turn in your `credentials.ini` using Canvas, which will point to your repository on GitHub, which should contain:

* Dockerfile

* The working application.

* A `README.md` file that includes not only identifying information (your name, email, etc.) but but also a revised, clear specification of the brevet controle time calculation rules.

* An automated 'nose' test suite.

## Grading Rubric

* If your code works as expected: 100 points. This includes:

	* Completing the frontend in `calc.html`.
	
	* Completing the Flask app accordingly (`flask_brevets.py`).
	
	* Implementing the logic in `acp_times.py`.
	
	* Updating `README` with a clear specification.
	
	* Writing at least five correct tests using nose (put them in `tests`, follow Project 3 if necessary) and all pass.

* If the logic in `acp_times.py` is wrong or is missing, up to 30 points will be docked off.

* If the test cases are not there, are invalid or fail, up to 15 points will be docked off.

* If `README` is not clear, missing or not edited, up to 15 points will be docked off.

* If none of the functionalities work, 30 points will be given assuming `credentials.ini` is submitted with the correct URL of your repo and `Dockerfile` builds and runs without any errors.
    
* If `Dockerfile` is missing, doesn't build or doesn't run, 10 points will be docked off.
	
* If `credentials.ini` is not submitted or the repo is not found, 0 will be assigned.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.