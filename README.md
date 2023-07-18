# song-search-engine

The project is aim to develop a song search engine integrated with Rei-Ying KTV system.

## Build
```
docker build -t song-search-engine:latest .
```

## Run
```
docker run --name my-song-search-engine -dp 5000:5000 song-search-engine
```

## Monitor
```
docker logs -f my-song-search-engine
```