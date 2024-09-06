FROM node:lts-alpine3.20
WORKDIR /typoscript
COPY package*.json ./
RUN npm install -g pnpm
RUN npm install
COPY . .
RUN npm test

WORKDIR /
RUN apk update && apk add bash
COPY run_tests.sh ./
RUN chmod +x /run_tests.sh
ENTRYPOINT ["/bin/bash", "-s"]