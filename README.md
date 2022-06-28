## DigiScript

A digital script project for queueing theatrical shows

### Getting started

#### Client

This installs and builds the client side files (nvm recommended)

```shell
cd client
npm ci
npm run build
```

#### Server

This installs the Python requirements needed to run the server (pyenv recommended)

```shell
cd server
pip install -r requirements.txt
```

### Running

This starts the web server listening on port 8080

```shell
cd server
./main.py
```