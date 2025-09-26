# Mars Weather Tracker

A Python scripting project that fetches and visualises real weather data from NASA’s InSight Mars lander using their RESTful API.  
This project was built to practise Python scripting, file handling, API requests, and data visualisation. In addition to this, I dived into the world of Docker - this can be seen in my effort to make this application compatible with docker containerisation. Finally, I've also made my own CI/CD pipeline with GitHub actions within this repo - this includes writing my own unit and integration tests.

---

## Features
- Fetches weather data from NASA’s [InSight: Mars Weather Service API](https://api.nasa.gov/).
- Lists available Sols (Martian days) with their matching Earth dates.
- Shows detailed weather stats (average, min, max temperatures) for a chosen Sol.
- Visualises temperature stats for the last 7 Sols using `matplotlib`.
- Docker Compatibility for containerised execution (To do this, please follow the README.DOCKER.md instructions)

---

## Requirements:
- requests & matplotlib - These python libraries are REQUIRED to be installed
- Generate your private API key through NASA: (https://api.nasa.gov/)
- Add it to your enviroment by typing the command in your terminal in the directory of this folder: `export NASA_API_KEY="YOUR_API_KEY_HERE"` or creating a .env file in the projects directory

## To run the application:
 - Clone this repo into your enviroment
 - Make sure to read the Requirements section
 - Navigate to the project directory
 - run `python run.py`
