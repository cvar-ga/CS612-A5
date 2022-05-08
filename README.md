# CS612-A5
This is Assignment 5 for CS612. This is a web server which obtains customer information, including their orders, via a Flask RESTful API. The API and the web server run in separate Docker containers, which are managed via Docker-compose. To run this server, you must have Docker and Docker-Compose installed, along with NodeJS, npm, and npx.

To run the server, run the command ```docker-compose up --build``` from the root of the repo.

The endpoints that have been implemented in the API are as follows:

- /customers, which outputs the entire hard-coded JSON database
- /customers/ID, which outputs information regarding a single customer
- /customers/ID/orders, which outputs the list of a specific customer's orders
- /customers/ID/orders/ID, which outputs a single order belonging to a single customer.
