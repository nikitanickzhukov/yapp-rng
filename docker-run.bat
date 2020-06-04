docker build --file Dockerfile --tag yapp-rng:prod . && ^
docker run --publish 8010:80 --name yapp-rng-prod yapp-rng:prod
