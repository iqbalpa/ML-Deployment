docker build -t iqbalpa/image-model:v1 .
docker run -p 8080:8000 --name image-model iqbalpa/image-model:v1

# command to push the docker image to dockerhub