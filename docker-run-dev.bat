@echo off
set cwd=%~dp0
set vol=%cwd%app:/usr/local/app
echo %vol%

docker build --file Dockerfile-dev --tag yapp-rng:dev . && ^
docker run --rm --volume %vol% --publish 8010:80 --name yapp-rng-dev yapp-rng:dev
