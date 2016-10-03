# clean-flask-container

Fork this and add your app to the `app/` directory. To use this, just add your app and then use the docker-compose file. Here is a simple way of doing this.

```
alias fig="docker-compose"

fig up --build -d   #Run the container

#Check it out, edit your code, talk about it

fig down   #Stop and remove everything
```

Wash rinse repeat. Add all the bells and whistles you want.
