# clean-flask-container

Fork this and add your app to the `app/` directory. To use this, just add your app and then use the docker-compose file. Here is a simple way of doing this.

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
