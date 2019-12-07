# Usage

## Docker

Run the following command to build an image based on the Dockerfile and the next line to deploy the web app in the port 5000.
```bash
docker build -t hw7 .
docker run -d -p 5000:5000 hw7
```

## Experiment

To run the experiment, simply go to http://localhost:5000/ after running the Docker commands mentioned above. 
The data file is read and the flask web app shows the results. 
The expected output is the list of most popular female names for all ethnicities in 2016. 

## Data

The data I used is the Popular Baby Names from https://catalog.data.gov/dataset/most-popular-baby-names-by-sex-and-mothers-ethnic-group-new-york-city-8c742