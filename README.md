[![Code Coverage](https://codecov.io/gh/carsonclarke570/octopus-api/branch/master/graph/badge.svg)](https://codecov.io/gh/carsonclarke570/octopus-api) ![Unit Tests](https://github.com/carsonclarke570/octopus-api/workflows/Unit%20Tests/badge.svg?branch=master)

# Octopus API

## Instructions

### Prerequisites

Prior to running the project please install `Docker`. 

The following environment variables should be set:
* `CLIENT_ID` - Spotify Client ID
* `CLIENT_SECRET` - Spotify Secret ID

### Running the API

The API is run in an Docker container. The base image is moderately sized so spinning up the container the first time might take some time. If you're new to Docker just run:

```
docker-compose up --build api
```

Docker will spin up the API and listen on `localhost:5000`.

**NOTE:** 
* Avoid directly running with Python as the API relies on Redis as a key-value store across it's multiple threads.
* If for some reason the `Initializing API` message prints multiple times, consult your nearest God/Goddess

## Development

For development we use `docker-compose`. This will bring up a set of services require to run and maintain an instance of Octopus.

### Redis Database

### MySQL Database

### MySQL Admin Pane

### SQL Files

In the `sql/` directory is a set of SQL scripts for bringing up, modifying and tearing down Octopus's database. 

When you first build the `db` service with `docker-compose` th
