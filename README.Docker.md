### Building and Running the Python Application Inside a Docker Container

There are **two ways** to get the application running inside a Docker container.

> This assumes you have Docker installed on your machine.

---

#### 1) Build and Run Locally

If you have cloned this repository, navigate to the project folder and build the Docker image:

`docker build -t <image_name> .`

Run the image inside a container, passing your NASA API key as an environment variable:

`docker run -it -e NASA_API_KEY="YOUR_NASA_API_KEY_HERE" <image_name>`
Replace YOUR_NASA_API_KEY_HERE with your actual NASA API key.

Optional: Automatically remove the container after it exits:

`docker run --rm -it -e NASA_API_KEY="YOUR_NASA_API_KEY_HERE" <image_name>`

#### 2) Pull and Run from Docker Hub

If you don’t want to build the image locally, you can pull the pre-built image from Docker Hub:

docker pull 0xnickm/mars-weather-report:<tag>
docker run -it -e NASA_API_KEY="YOUR_NASA_API_KEY_HERE" 0xnickm/mars-weather-report:<tag>

Replace <tag> with the desired version (e.g., commit SHA or latest).

This method saves time, as you don’t need to build the image from source.
