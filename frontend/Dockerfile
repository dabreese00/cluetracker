FROM node:16.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# to make npm test run only once non-interactively
ENV CI=true

COPY package.json /usr/src/app
RUN npm install && \
    npm install -g serve

COPY . /usr/src/app

# defined in package.json
CMD ["sh", "./entrypoint.sh"]
