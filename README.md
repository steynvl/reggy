# Reggy

Reggy is a general-purpose regular expression generator that is exposed as a web application. Reggy assists you with the construction of regular expressions. The generator consists of three components, each for a different use case. Reggy generates regular expressions for a wide variety of programming languages and strives to generate regular expressions that are as efficient and concise as possible.

## Prerequisites

* Install [Node.js](https://nodejs.org/en/) version 8.x
* Install Angular CLI: `sudo npm install -g @angular/cli`
* Install all the dependencies from the project root directory: `npm install`
* Install graphviz: `sudo apt-get install graphviz`
* Install pip: `sudo apt-get install -y python3-pip`
* Install python graphviz package: `sudo pip3 install graphviz`

## Development

`npm run dev`: This will [concurrently](https://github.com/kimmobrunfeldt/concurrently) execute the Angular build, TypeScript compiler and Express server.

A window will automatically be opened at [localhost:4200](http://localhost:4200). Angular and Express files are being watched. Any change will automatically create a new bundle, restart the Express server and reload your browser.

## Deploying to Heroku

The web app is deployed using [Docker](https://www.docker.com/), thus docker ce needs to be installed on the system.
```bash
sudo apt-get install docker-ce
```

#### Testing Docker build locally
Change the working directory to the root directory of the project which contains the Dockerfile and run the following:
```bash
sudo docker build -f Dockerfile -t reggy:latest . --network=host
```

```bash
sudo docker run -p 49160:3000 -d reggy:latest
```

#### Deploying
Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if it is not installed and then change the working directory to the root directory of the project.
```bash
heroku login
```
```bash
sudo heroku container:login
```
```bash
sudo heroku container:push web --app reggy
```
```bash
heroku container:release web --app reggy
```
