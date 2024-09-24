
# Reservamos Challenge

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About the Project](#about-the-project)
  - [Considerations](#considerations)
  - [Technical Considerations](#technical-considerations)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run without Docker](#run-without-docker)
  - [Environment Variables](#environment-variables)
  - [Environment Variables for UI](#environment-variables-for-ui)
  - [Change Ports](#change-ports)
    - [Change ports on Docker](#change-ports-on-docker)
    - [Change port on debug mode without docker](#change-port-on-debug-mode-without-docker)

## About the Project

This project is a weather API that uses the [Reservamos](https://www.reservamos.com/) API to fetch travel destinations and then connects to the [OpenWeatherMap](https://openweathermap.org/forecast5) Free API to fetch weather data for each destination.

### Considerations

- The initial requirement was to fetch 7-day forecast for a given destination using One Call API 3.0. Since the API key was disabled by the time of writing this project, I switched to the [OpenWeatherMap free API 5-day / 3-hour forecast.](https://openweathermap.org/forecast5)
  
- The free API returns a list of datetimes for every 3 hours for the next 5 days. I implemented a custom mechanism to fetch the data for each day, adding a custom environment variable to the `.env` file to fetch only for weather at 15:00. This can be changed to retrieve as many hours as you want, as long as they are multiples of 3.

- The free API has a limit of 1000 calls per day and 60 calls per minute. I implemented a custom mechanism to paginate destinations results, so the API can be used without any limitations or over-fetching during the development and testing phase. Pagination can be disabled by setting the `show_all` arg to `true` in the request params.

- I implemented a custom UI using [React](https://reactjs.org/) to display the weather data. The UI is a simple dashboard with a search bar and a list of destinations with their weather data. The purpose of this project is to demonstrate a visual application of the weather API.

### Technical Considerations

- The weather API will run by default on port 9000, and the UI on port 9001. This is to avoid conflicts with other Django projects running on the same port. If you want to change the ports, see the [Change Ports](#change-ports) section.
- The weather API is built using [Django](https://www.djangoproject.com/) and `requests` to fetch data from the Reservamos API and `httpx` to fetch data from the OpenWeatherMap API. The reason for using `httpx` is that the OpenWeatherMap API was rejecting the requests made by the `requests` library due to the lack of a user agent, openweatherapi might be slow if overfetching happens, there is a print statement in the code to show checkpoints between requests.

- The weather API documentation is built using [drf-yasg](https://github.com/axnsan12/drf-yasg) and [Django Rest Framework](https://www.django-rest-framework.org/) to generate the Swagger docs.
- The weather API is containerized using [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/). If you prefer to run the API without containers, see the [Run without Docker](#run-without-docker) section.

### Built With

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Reservamos](https://www.reservamos.com/)
- [OpenWeatherMap](https://openweathermap.org/)
- [React](https://reactjs.org/)
- [NextUI](https://nextui.org/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need to have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.

### Installation

1. Clone the repository
    ```sh
    git clone https://github.com/AlexRiosXI/ReservamosChallenge.git
    ```
2. Navigate to the project directory
    ```sh
    cd ReservamosChallenge
    ```
3. Create a `.env` file in the root directory of the project and add the following content *(you can see the [environment variables](#environment-variables) section)*:
    ```sh
    RESERVAMOS_API_URI="uri to reservamos places api"
    OPEN_WEATHER_API_URI="uri for open weather 5 day/3 hour api"
    OPEN_WEATHER_API_KEY="your open weather api key, this works with the free subscription plan"
    ```
4. Create a `.env` file in the `ui-api-demo` directory and add the following content *(you can read the `.env.example`)*:  
    ```sh
    VITE_API_URI="http://localhost:9000" # change this to your weather URL or port, default is 9000
    ```
5. Build the containers
    ```sh
    docker-compose build
    ```
6. Run the containers
    ```sh
    docker-compose up
    ```
7. Open Swagger docs in your browser
    ```sh
    http://localhost:9000/docs/
    ```
8. Open the UI in your browser
    ```sh
    http://localhost:9001
    ```

### Run without Docker

1. Clone the repository
    ```sh
    git clone https://github.com/AlexRiosXI/ReservamosChallenge.git
    ```
2. Navigate to the project directory
    ```sh
    cd ReservamosChallenge/api
    ```
3. Create a `.env` file in the root directory of the project and add the following content *(you can see the [environment variables](#environment-variables) section)*:
    ```sh
    RESERVAMOS_API_URI="uri to reservamos places api"
    OPEN_WEATHER_API_URI="uri for open weather 5 day/3 hour api"
    OPEN_WEATHER_API_KEY="your open weather api key, this works with the free subscription plan"
    ```
5. Create a Python virtual environment
    ```sh
    python -m venv env
    ```
6. Activate the virtual environment
    ```sh
    source env/bin/activate # on Linux
    env\Scripts\activate # on Windows
    ```
7. Install the requirements
    ```sh
    pip install -r requirements.txt
    pip install setuptools # might be needed on some Python versions
    ```
8. Run the API
    ```sh
    python manage.py runserver
    ```
9. Open Swagger docs in your browser
    ```sh
    http://localhost:9000/docs/
    ```

### Environment Variables

| Variable Name       | Description                                  | Default Value                                         |
|---------------------|----------------------------------------------|-------------------------------------------------------|
| RESERVAMOS_API_URI  | URI to Reservamos API                        | https://search.reservamos.mx/api/v2             |
| OPEN_WEATHER_API_URI| URI to OpenWeatherMap API                    | https://api.openweathermap.org/data/2.5/forecast       |
| OPEN_WEATHER_API_KEY| OpenWeatherMap API Key                       | Free Subscription API Key                             |
| WEATHER_HOUR_FILTER         | Hours to fetch weather data (comma separated) enum: 3,6,9,12,15,18,21 | 15                                     |

### Environment Variables for UI

| Variable Name | Description      | Default Value           |
|---------------|------------------|-------------------------|
| VITE_API_URI  | URI to Weather API | http://localhost:9000 |

### Change Ports

#### Change ports on Docker

1. Open the `docker-compose.yml` file and change the ports to the desired ports.

    ```yaml
    ...
    ports:
      - "{PORT}:9000"
    ```

#### Change port on debug mode without docker

1. Start the server using the following command:
    ```sh
    python manage.py runserver 0.0.0.0:{PORT}
    ```
