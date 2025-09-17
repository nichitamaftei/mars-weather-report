### Building and running your application

When you're ready, start your application using docker containers by navigating to the project folder and either:
`docker compose up --build` to build the image and run it one step
OR:
`docker build -t <image_name> .` AND `docker run -it -e NASA_API_KEY="YOUR_NASA_API_KEY_HERE" <image_name>` to build an image and run the image respectively


### References
* [Docker's Python guide](https://docs.docker.com/language/python/)