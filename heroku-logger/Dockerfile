FROM node:lts-alpine3.20
WORKDIR /heroku-logger
COPY package*.json ./
RUN npm install -g pnpm
COPY . .
RUN npm install
RUN npm test

WORKDIR /
RUN apk update && apk add bash
COPY run_tests.sh ./
RUN chmod +x /run_tests.sh
ENTRYPOINT ["/bin/bash", "-s"]