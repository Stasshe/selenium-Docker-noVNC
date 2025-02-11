
```
docker run -d --name selenium \
  -p 4444:4444 -p 7900:7900 \
  --shm-size=4g \
  -e SE_NODE_SESSION_TIMEOUT=3000 \
  -e SCREEN_WIDTH=1280 \
  -e SCREEN_HEIGHT=720 \
  -e SCREEN_DEPTH=24 \
  selenium/standalone-chrome
```





使わない
docker pull stasshe/selenium-standalone-chrome:latest
