## This project is a Streamlit frontend that orchestrates multiple FastAPI microservices (stock analysis, market news, portfolio, earnings) which then fetch data from Alpha Vantage, registered/discovered via a Consul-backed service registry, all containerized with Docker Compose.

## This application is made utilizing the microservice architecture.

## Running the docker compose will start up multiple containers for each service present, which you can add and remove dynamically.

## Link- [Project Demo](https://github.com/ShikharSrivastava-aiml/StocksResearchDashboard/raw/main/Project%20Demo_%20Microservices%20in%20Action.mp4)

## To run the application enter the following commands in terminal:

git clone https://github.com/ShikharSrivastava-aiml/StockResearchDashboard.git

docker-compose up --build

## Running Tests
Running tests creates pycache files. There are 39 tests all in the tests/ directory.
For more info about the tests visit our project documentation or look at the comments in test files.
To run the test suite, use the following command:

python -m pytest

