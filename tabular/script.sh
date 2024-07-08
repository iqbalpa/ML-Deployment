docker build -t iqbalpa/tabular-model:v1 .
docker run -p 8080:8000 --name tabular-model iqbalpa/tabular-model:v1

# command to push the docker image to dockerhub