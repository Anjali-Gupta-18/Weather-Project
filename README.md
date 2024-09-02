# City Weather Tracker with Real-Time Data

## Project Overview
The City Weather Tracker application provides real-time weather data for various cities. It features a backend API developed using Django that integrates with the Open Weather API to fetch up-to-date weather information. Users can add new cities to a list and view current weather data for all cities stored in the database.

## Features
- Real-time weather updates for multiple cities.
- Add new cities to the weather tracking list.
- View current weather conditions for all cities.
- Backend API built with Django and integrated with the Open Weather API.

## Skills and Technologies
- **Django**: Framework for developing the backend API and managing the database.
- **API Integration**: Utilizes the Open Weather API to retrieve real-time weather data.
- **Python**: Core programming language used for backend development.
- **SQL**: Database management for storing city and weather data.

## Installation
To set up the City Weather Tracker, follow these steps:

1. Clone the repository:
   git clone https://github.com/Anjali-Gupta-18/Weather-Project
   cd city-weather-tracker
2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
      pip install -r requirements.txt
4. Set up the database:
     python manage.py migrate
5. Start the development server:
      python manage.py runserver

Project Structure
weather_tracker/: Main Django application folder.
weather_tracker/settings.py: Django settings configuration.
weather_tracker/urls.py: URL routing for the application.
weather_tracker/views.py: Views handling the API and web requests.
requirements.txt: List of dependencies.


Acknowledgments
Open Weather API: For providing real-time weather data.
Django: For the powerful web framework that supports the backend.
