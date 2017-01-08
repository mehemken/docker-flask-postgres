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

#Check it out, edit your code, talk about it

fig down   #Stop and remove everything
```

Wash rinse repeat. Add all the bells and whistles you want.

#Recycling

Github does not let you fork your own repositories. So if you fork this and then decide you want to make use of it multiple times for different projects you do this.

```bash
git clone <this repo>
git remote remove origin
```

Now you can work on this without worrying that you might do an accidental `git push` and mess with the original repo. If you want to add a new origin, see the documentation for working with git remotes.
