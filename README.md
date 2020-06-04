# YAPP - Random Number Generator
A microservice responsible for generating random numbers

## User story
- shuffle a sequence of numbers in certain range

## Implementation
- Gunicorn Web Server: https://gunicorn.org/
- Falcon Web Framework: https://falconframework.org/
- Python `random` library

## Deployment
- `./docker-run.bat` - building and running container for production
- `./docker-run-dev.bat` - building and running container for development (direct code mounting, hot reload)

## API docs
http://localhost:8010/v1/docs

## Dependencies
No
