# docker-flask-postgres

This is a simple demo for how to connect to a Postgres database from a python flask application. To run this on your computer you must first install [docker](https://docs.docker.com/engine/installation/).

##Running

First do a ```git clone```.

    git clone https://github.com/mehemken/docker-flask-postgres

Then make sure you have docker [installed](https://docs.docker.com/engine/installation/). I also recommend [docker-compose](https://docs.docker.com/compose/install/) to make life easier, but it comes with docker engine for Windows and Mac.

Once you have all of that, you should be good. No need to install [Postgres](https://www.postgresql.org/) or even Python.

```
alias fig="docker-compose"

fig up --build -d   #Run the container

fig down   #Stop and remove everything

# Add your code to the /app/ directory
# At the moment, you have to do a fig up/down after each change.
# However, I'll be adding support for a dev setting
# where all you'll need is to refresh the page in your browser.
```

Wash rinse repeat. Add all the bells and whistles you want.

