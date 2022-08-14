# Ridecell Assignment

A minimal web app developed with [Flask](http://flask.pocoo.org/) framework. 

The main purpose is to showcase a very basic book shipment tracking web application with Flask, with the aim to demonstrate:

- Microservice Architecture

- Interaction between different microservices

- Template & Template Inheritance

- Error Handling

- Integrating with *Bootstrap*

- Interaction with Database (SQLite)

- Invoking static resources


## What's missing

Due to time constraints, I could not implement a few features I had in mind including:

- OAuth2 and authentication

- Tracking sessions

- Unit tests and Behaviour-Driven Development scenarios

- UI-based enhancements

## How to Run

- Step 1: Make sure you have Python 3.6+

- Step 2: Install the requirements: `pip install -r requirements.txt`

- Step 3: Go to this app's directory and run `python run.py`



## Details about This Tracking App

There are three microservices in this app:

- **rdc_frontend_service**: this is an asset collection microservice currently with no functioning APIs. It contains static JS, CSS, HTML, Jinja templates and a Swagger file to power the Frontend.

- **rdc_orders_service**: this contains orders.db which serves as the database of all the orders as well as an utility to interact with the DB. Further, a couple of APIs to update and fetch records from the DB.

- **rdc_shipment_tracker_service**: this contains the shipment tracking API; which essentially interacts  with the external third party API. It also has a mock simulation API to simulate the results of the third party API for the purpose of this assignment.

I have designed the structure of the project with facade pattern and modularity in mind. Even though wrappers and utilities are not present in the current project, due to the scope of this project, they can be easily added.

The dummy services currently added are not limited to the scope of this tracking application but can further be used by other microservices. Some path changes could be needed as per the OS.

#### Please feel free to contact me if you have any questions about the same ####