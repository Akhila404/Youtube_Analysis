# YouTube Analysis Project:-

This project is a comprehensive analysis and prediction tool designed to provide insights into YouTube videos. The tool is developed using Flask and integrates various data analytics and machine learning techniques to predict the number of likes a YouTube video might receive based on specific input features such as views, dislikes, comment counts, and genre.

The project also includes a Tableau dashboard for visualizing data, making it a powerful resource for anyone looking to understand or predict video performance on YouTube.

### Features:
**Home Page:**
A welcoming interface that provides navigation to various sections of the application.

**Contact Us Page:**
A user-friendly form where users can submit their details and inquiries. After submission, users are redirected to a Thank You page with a confirmation message.

**YouTube Likes Predictor:**
This tool allows users to input data such as views, dislikes, comment counts, and video genre to predict the number of likes a video might receive using a Random Forest Regression model.

**Analytical Dashboard:**
An embedded Tableau dashboard that provides a visual representation of the data and insights derived from it.

**Result Page:**
Displays the predicted number of likes based on the input provided by the user.

**Thank You Page:**
A confirmation page that acknowledges the user after they've made contact through the form.


### Pages Overview:
**home.html:** 
The landing page with navigation links to other sections like YouTube Analysis, Like Predictor, and Contact Us.

**contactus.html:**
The contact form page where users can enter their full name, phone number, email, address, and a message.

**likePredictor.html:**
The page where users can input data to predict the number of likes a video will receive. It includes a dropdown for video genres with options such as 'Autos & Vehicles', 'Comedy', 'Education', etc.

**result.html:**
After the user submits data on the Like Predictor page, this page displays the predicted number of likes.

**thankyou.html:**
Redirects users here after submitting a contact form, with a message stating that they will receive a response within 24 hours.


### Deployment:--
The project is deployed on Render.com, making it accessible for live demonstrations and use. You can access the live application using the following link: https://youtube-analysis-siy6.onrender.com

### How to Use?
**Navigate to the Home Page:** Explore the different sections.

**Use the Like Predictor:** Input relevant data and click submit to see the predicted likes.

**Check the Analytical Dashboard:** View comprehensive analytics through the Tableau dashboard.

**Contact Us:** Submit any inquiries and receive a confirmation message.


### Project Structure:--
**app.py:** The main Flask application script.

**templates/:** Directory containing all HTML files including home.html, contactus.html, likePredictor.html, result.html, and thankyou.html.

**datacleaning.ipynb:** This notebook handles the preprocessing and cleaning of the YouTube dataset, including tasks like handling missing values, encoding categories, and normalizing data to prepare it for model training and analysis.

**model.ipynb:** This file implements a predictive model using the Linear Regression algorithm for predicting YouTube video likes.

**test.ipynb:** This file sets up the database for the Contact Us section, storing all customer inquiries.
