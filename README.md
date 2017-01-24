# skel-python-service
> _A Skeleton Python Service._

## Introduction
This is the simplist microservice ever.

## Pre-requisits
The application is run with `docker` and `docker-compose`. Please use the following links to install.

 * [docker][1]
 * [docker-compose][2]

## Runing the Application
First clone the repository with:
 ```bash
 git clone https://github.com/diversemix/skel-python-service.git
 ```

Then change to the root folder then build and start with docker-compose:
 ```bash
 cd skel-python-service
 docker-compose build
 docker-compose up -d
 ```
## Testing

You can change the message in: `config.json`
```
curl localhost:5000/v1/status
```

Now for a POST
```
curl -X POST -H "Content-Type: application/json" --data "[1,2,3]" localhost:5000/v1/query
```

[1]: https://docs.docker.com/engine/installation/
[2]: https://docs.docker.com/compose/install/
