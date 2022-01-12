FROM node:lts-alpine as build-stage

WORKDIR /app

COPY package*.json ./

RUN npm install -g @vue/cli

COPY . .

RUN npm install
