FROM ubuntu:16.04

RUN apt-get -qq update
RUN apt-get install locales

# install curl
RUN apt-get install -y curl

# download node.js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

# install node.js
RUN apt-get install -y nodejs

# ensure npm packages can build
RUN apt-get install -y build-essential
RUN apt-get install -y git-core

# install graphviz
RUN apt-get install -y graphviz
RUN apt-get install -y python3-pip
RUN pip3 install graphviz

COPY . usr/src/app
WORKDIR /usr/src/app

# install app dependencies, compile server and build the angular client
# with production and aot compilation flags
RUN npm install --only=prod

# expose port 3000 for node application
EXPOSE 3000

# run server
CMD [ "node", "dist/server/app.js" ]
