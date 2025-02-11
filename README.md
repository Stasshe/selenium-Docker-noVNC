```
docker build -t my-selenium-app .
```


```
docker run -d --name selenium -p 4444:4444 -p 7900:7900 --shm-size=2g my-selenium-app
```