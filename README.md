### Run application with docker ###

- build image
`docker build -t sample .`
- run container
`docker run -d -p 8000:8000 --name sample sample`