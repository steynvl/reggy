# Reggy

## Prerequisites

* Install [Node.js](https://nodejs.org/en/) version 8.x
* Install Angular CLI: `sudo npm install -g @angular/cli`
* Install all the dependencies from the project root directory: `npm install`

## Development

`npm run dev`: This will [concurrently](https://github.com/kimmobrunfeldt/concurrently) execute the Angular build, TypeScript compiler and Express server.

A window will automatically be opened at [localhost:4200](http://localhost:4200). Angular and Express files are being watched. Any change will automatically create a new bundle, restart the Express server and reload your browser.

## Deployment

The web app is built and shipped using [Docker](https://www.docker.com/), thus docker ce needs to be installed on the system.

#### Building the image
Change the working directory to the root directory of the project which contains the Dockerfile and run the following:
```bash
sudo docker build -t regy:latest . --network=host
```

#### Running the container
```bash
sudo docker run -p 49160:3000 -d regy:latest
```
