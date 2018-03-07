# docker-flask-postgres

This is a simple demo for how to connect to a Postgres database from a python flask application. To run this on your computer you must first install [docker](https://docs.docker.com/engine/installation/).

## Running

First fork the repo then do a `git clone`.

    git clone https://github.com/<yournamehere>/docker-flask-postgres

You should also have [docker](https://docs.docker.com/install/). If you're on linux, you probably also want docker-compose. Last I checked (over a year ago) it did not come with docker by default. For Mac and Windows you get it with the default installation.

Once you have all of that, you should be good. No need to install [Postgres](https://www.postgresql.org/) or even Python.

```
docker-compose up --build -d   # Run the container.

docker-compose down   # Stop and remove everything.

# Add your code to the /app/ directory.
# At the moment, you have to do a fig up/down after each change.
```

The site will be available to you at `localhost:43434`.

If you have questions, I'm on twitter @mehemken. I encourage you to let me know what you use this for and how I could make it easier for you to use.

## One year later

So this got forked. I'm surprised but I'm glad someone found it useful. Then I got nervous thinking "uh oh, does this actually work?". I just follwed the above instructions and I'm happy to report that, yes. It does still work. :)

Three months since this and a few more forks. Hmm... I'm going to have to clean this up a little bit. And use a more up to date docker-compose. And add tests...


## How it works

There are two Dockerfiles. One is the base Dockerfile that has Python and Flask. I've separated that one out so you don't have to keep downloading Python and Flask over and over again. The second one is the application Dockerfile. This is the one that will get updated frequently as you make changes to your Flask app. I found this to be a faster, more convenient iteration cycle for when I was building it.

The `docker-compose.yml` file tells Docker that you need your Flask container and a Postgres container.
