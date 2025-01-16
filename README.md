# Andy Cafe Website

This project is the website for Andy Cafe, a cafe located in San Pablo City, Calabarzon, Philippines. It allows customers to place orders online and provides an administrative interface for managing those orders.

## Overview

The website provides a user-friendly way for customers to browse the menu, place orders, and for administrators to manage those orders. The site emphasizes visual appeal and a simple, intuitive user experience.

## About Us
Greetings from Andy Cafe, your local sanctuary for coffee enthusiasts and others. 
We have a strong desire to create outstanding drinks and a welcoming environment. 
From traditional espressos to creative custom blends, our committed baristas skillfully craft a wide range of coffee beverages.
We have something to suit every taste, whether you want a smooth, mild brew or a strong, black roast.

## Key Features

*   **Online Ordering:** Customers can place orders through an online form, selecting from various food and beverage options, including hot and cold beverages, meals, pasta, burgers, and fries.
*   **Order Management:** user have access to a page where they can view, edit, and delete orders.
*   **Order Details:** The system stores and displays key order information:
    *   Order ID
    *   Customer Name
    *   Contact Number
    *   Address (San Pablo City, Calabarzon, Philippines)
    *   Ordered Items (Hot Beverages, Cold Beverages, Meals, Pasta, Burger & Fries)
*   **Location Specificity:** The website is tailored to customers in San Pablo City, Calabarzon, Philippines.

## Links
*   **facebook:** https://www.facebook.com/profile.php?id=61570357920747&mibextid=ZbWKwL
*   **Instagram:** https://www.instagram.com/cafeandy1?igsh=MWw5bmVvM3U5Ymkx
*   **Github:** https://github.com/Lendsproject/Website/new/main?filename=README.md
*   **Web Link:** 



## Technologies Used

*   **Frontend:** HTML, CSS, 
*   **Backend:** Python (likely Flask )
*   **Database:** MySQL
*   **Web Server:** Apache 

## Usage (For Customers)

1.  Visit the website.
2.  Navigate to the "Order" page.
3.  Fill out the order form with your details and desired items.
4.  Submit your order.

## Connect to the Devs
1.  [Castillo, Lendrick M. BSIT](https://www.facebook.com/lendrick.castillo.9)
2.  [Tan, Andy Jr A. BSIT](https://www.facebook.com/andyjr.tan.5?mibextid=ZbWKwL)


## Flask Web Application with Integrated API
This document explains how an API (Application Programming Interface) integrates with a Flask web application.

What is an API?
An API allows different software systems to communicate with each other. In a Flask application context, the API handles requests from the client (like a web browser) and responds with data or performs actions on the server.

## How the API Integrates
The API works alongside the website, not as a replacement. Here's how they work together:

1. Defining Routes
Routes in Flask are defined using the @app.route decorator. Each route corresponds to a URL endpoint that the client can access.

![image](https://github.com/user-attachments/assets/94daae4c-6c13-45d8-b22f-7ac0966de544)

- These routes define endpoints for the home and about pages of your website. When a user navigates to these URLs, the corresponding functions are executed, and the appropriate HTML templates are rendered.


2. Handling Requests
Flask can handle different types of HTTP requests, such as GET and POST. For example, the /order route can handle both GET and POST requests:

![image](https://github.com/user-attachments/assets/97b91924-af05-434c-8690-69a99bb31dc7)

- GET Request: When the user navigates to /order, the server responds with the order.html template.
- POST Request: When the user submits the order form, the server processes the form data and redirects to the home page.


3. Interacting with the Database
The Flask application can interact with a MySQL database using the flask_mysqldb extension. For example, you can insert form data into the database:

![image](https://github.com/user-attachments/assets/b3192859-5ab1-4908-b314-aa8e767431ec)

4. Returning JSON Responses
For API endpoints that return data (e.g., for a JavaScript frontend), you can return JSON responses:

![image](https://github.com/user-attachments/assets/91099b21-e34b-4c91-91cc-e71822ae153e)

5. Error Handling
Flask can handle errors and provide appropriate responses:

![image](https://github.com/user-attachments/assets/0aa9b1b0-f4bc-49d5-b734-f7999b6979ed)

## Summary
*  **Routes:** Define URL endpoints.
*  **Request Handling:** Process GET and POST requests.
*  **Database Interaction:** Perform CRUD operations on the database.
*  **JSON Responses:** Return data for API endpoints.
*  **Error Handling:** Manage errors and provide user-friendly messages.
  
By integrating these components, Flask application can serve dynamic content, handle user input, interact with a database, and provide data through an API.


## API Documentation

This section documents the API endpoints.

### Create a New Order

This endpoint creates a new customer order.

**URL:**

`/api/add`

**HTTP Method:**

`POST`


**Request Body:**

```json
   {
     "type": "object",
     "properties": {
       "Customer Name": { "type": "string", "description": "The name of the customer placing the order." },
       "Contact Number": { "type": "string", "description": "The customer's contact number." },
       "Hot Drinks": { "type": "string", "description": "Hot drinks ordered (e.g., \"Caramel Machiato\", \"Americano\")." },
       "Cold Beverages": { "type": "string", "description": "Cold beverages ordered (e.g., \"Caramel Machiato\", \"Matcha Latte\")." },
       "Ordered Meals": { "type": "string", "description": "Meals ordered (e.g., \"Tapsilog\", \"Bacsilog\")." },
       "Ordered Pasta": { "type": "string", "description": "Pasta dishes ordered." },
       "Ordered Burger & Fries": { "type": "string", "description": "Burger and fries ordered." }
     },
     "required": [ "Customer Name", "Contact Number" ]
   }


**Sample Request:**

JSON
   
   {
     "Customer Name": "Andy",
     "Contact Number": "09823547891",
     "Hot Drinks": "Americano",
     "Cold Beverages": "Green Apple",
     "Ordered Meals": "Tapsilog",
     "Ordered Pasta": "Pesto Pasta",
     "Ordered Burger & Fries": "Beef Burger & Fries"
   }

**Sample Response:**

JSON

{
  "Order_id": 1,
  "Customer Name": "Andy",
  "Contact Number": "09823547891",
  "Hot Drinks": "Americano",
  "Cold Beverages": "Green Apple",
  "Ordered Meals": "Tapsilog",
  "Ordered Pasta": "Pesto Pasta",
  "Ordered Burger & Fries": "Beef Burger & Fries"
}

