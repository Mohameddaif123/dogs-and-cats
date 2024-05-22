Pet Store Django Redux Application
Welcome to the Pet Store Django Redux application! This advanced application allows users to browse, purchase, and manage pet products through an intuitive web interface. It combines the power of Django on the backend with Redux on the frontend to provide a seamless and robust user experience.

Table of Contents
Features
Installation
Backend Setup
Frontend Setup
Usage
Technologies Used
Contributing
License
Features
User Authentication: Users can register, log in, and log out securely.
Product Management: Admin users can add, edit, and delete pet products.
Shopping Cart: Users can add products to their cart and proceed to checkout.
Order Management: Admin users can manage orders and mark them as fulfilled.
Responsive Design: The application is optimized for various screen sizes and devices.
Installation
To run this application locally, follow the instructions below to set up the backend and frontend environments.

Backend Setup
Clone the repository to your local machine:

bash
Copy code
git clone <repository_url>
cd <repository_name>
Create a virtual environment and activate it:

bash
Copy code
virtualenv venv
source venv/bin/activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Apply the migrations and create a superuser:

bash
Copy code
python manage.py migrate
python manage.py createsuperuser
Start the Django development server:

bash
Copy code
python manage.py runserver
Frontend Setup
Navigate to the frontend directory:

bash
Copy code
cd frontend
Install the required Node.js packages:

bash
Copy code
npm install
Start the React development server:

bash
Copy code
npm start
Usage
Once both the backend and frontend servers are running, you can access the application by navigating to http://localhost:3000 in your web browser. From there, you can:

Register a new account or log in with an existing one.
Browse the available pet products and add them to your cart.
Proceed to checkout and complete your purchase.
Admin users can access the admin dashboard (http://localhost:8000/admin) to manage products and orders.

Technologies Used
Backend
Django: A high-level Python web framework for backend development.
Django REST Framework: A powerful toolkit for building Web APIs in Django.
Unit Testing: Django provides built-in support for unit testing with its unittest module.
Frontend
React: A JavaScript library for building user interfaces.
React Router: A routing library for React applications.
Redux: A predictable state container for managing the application's state.
React-Redux: Official React bindings for Redux.
React-Toastify: A simple and flexible toast notification library for React applications.
Additional Frontend Libraries
@emotion/react
@emotion/styled
@mui/material
@mui/icons-material
@paypal/react-paypal-js
@reduxjs/toolkit
@testing-library/jest-dom
@testing-library/react
@testing-library/user-event
antd
axios
jwt-decode
react-adsense
react-burger-menu
react-dom
react-helmet
react-icons
react-redux
react-router-dom
react-scripts
react-toastify
redux-logger
web-vitals
Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. Feel free to modify and distribute the code for your own purposes.

Admin credentials:

Username: hadi
Password: 123
Admin/superuser will see more buttons and will be able to perform additional actions such as updating, removing, and adding new products.

