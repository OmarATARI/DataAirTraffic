# Getting Started

Launch docker containers:
```
docker-compose build
docker-compose up -d
```

Populate database:
```
docker-compose run --rm flask-visualization python3 generate_data.py 
```
