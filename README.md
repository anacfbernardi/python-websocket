# Advanced Computing Challenge

## General instructions

* The solution should be inside trading-aggregator and trading-broadcaster folders
* The trading-aggregator and trading-broadcaster folders contains an .env file. This file should be included in the dist folder during the build process and should contain 2 variables:
  * WS_CONSUMER_PORT is the PORT where the websocket server will be hosted (i.e. consumers should connect to this port on localhost). Your solution should read this port and create the server based on the .env file. Please note that we may have multiple instances of the Trading Aggreagator, so it is important that the solution can read the values from the .env file.
  * WS_STORAGE_API_PORT (default 3000) is the PORT where the storage API is hosted. The storage API can be accessed by making a HTTP request to http://localhost:{PORT}/api/{path}.
* A sample of the API to store the latest prices is available on storage-api folder. In this folder you can see all endpoints provided by the Storage API. There is no need to change anything in that folder.
* A sample of the data-provider is available on data-provider folder. You can use that in your tests

## Build the solution
This solution requires Python 3.10 and Poetry 1.1 installed.

To build the solution just install the python dependencies
```shell
poetry install
```

## Run solution locally
To run the solution locally (start server on port 3000) just run this command
```shell
poetry run python app.py
```