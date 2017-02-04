# Back-End Branch

This branch contains functionality for the database and API. It will be eventually be merged with `master`.

Our goal is to create a tool that allows the public to easily understand and explore the state of housing in Portland.
In the meantime...

### Requirements

* [Docker](https://www.docker.com/products/overview)

Unless you have a recent Mac, Windows 10 Professional, or Linux, you'll have
to use Docker Toolbox, which is temperamental and not covered here. As a
workaround, you can run Docker in a Vagrant box using these tools:

* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant for Docker](https://github.com/JohnTasto/vagrant-for-docker)

### Download

Clone the repository from the command line:
```sh
$ git clone git@github.com:hackoregon/housing-17.git
```

Navigate to the backend branch:
```sh
$ cd housing-17
$ git fetch origin backend
$ git checkout backend
```

### Run

#### Bash/Zsh/etc

##### Start:
```sh
$ ./dj.sh up
```

##### Shutdown:
```sh
$ ./dj.sh down
  # or
$ ./dj.sh down --rmi   # remove images to save disk space
```

##### Rebuild images (necessary if `requirements.txt` changes):
```sh
$ ./dj.sh down   # (if not already shut down)
$ ./dj.sh up --build
```

##### Run manage.py command directly:
```sh
$ ./dj.sh manage <command>
```

#### Windows (or Bash/Zsh/etc....)

##### Start:

Run Django and PostgreSQL detached (running in the background):
```sh
$ docker-compose up -d
```

Migrate database:
```sh
docker-compose exec web ./manage.py migrate
```

Load data:
```sh
docker-compose exec web ./manage.py shell --command="import housing_backend.loader"
```
This might take a little while since we're loading the data into the database.

##### Shutdown:
```sh
$ docker-compose down
  # or
$ docker-compose down --rmi all   # remove images to save disk space
```

##### Rebuild images (necessary if `requirements.txt` changes):
```sh
$ docker-compose down   # (if not already shut down)
$ docker-compose up --build
```

##### Run manage.py command directly:
```sh
docker-compose exec web ./manage.py <command>
```

### Develop!

Have at it! Feel free to explore the [API docs](https://github.com/hackoregon/housing-17/tree/backend/docs/API.md)
