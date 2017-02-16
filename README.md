# Hack Oregon Housing Project, 2016-2017
This project will create a dynamic, educational portal that helps clarify the multifaceted and changing rental environment in PDX, with a focus on affordable rentals. The team will investigate what parts of town are currently affordable to a diverse spectrum of residents, and explore trends in how the Portland housing and rental market has changed over time, with a special emphasis on recent changes in the 7-year census gap. The project will approach common perceptions of the state of affordable rent in Portland with a range of digital, analytical, and creative strategies, with the overall goal of broadening insight on the experience of renting in Portland.
The most current version of Team Housing's Vision Document / Elevator Pitch is maintained by Gabriele Hayden.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

```
# From your local machine, set up Git
# From GitHub, set up GitHub Authentication
# From GitHub, fork the Repo at `https://github.com/hackoregon/housing-17`

# Clone the GitHub repository using SSH or HTTPS
$ git clone git@github.com:YOUR-USERNAME/housing-17.git
# or...
$ git clone https://github.com/YOUR-USERNAME/housing-17.git

# Report branches and files
$ git status

# Refresh
$ git pull origin master

# List the current branches of the repository
$ git branch -a

# Check out a feature branch
$ git checkout backend

# Create a new feature branch
$ git branch mynewfeature

# Do some coding...

# Add or update files
$ git add -A

# Commit the changes
$ git commit -m "my changes"

# Push changes to the new feature branch
$ git push origin mynewfeature

# To initiate a merge of your new feature, from GitHub choose Pull Request

# Switch to a different branch
$ git checkout master

```

### Prerequisites

If you are running a recent edition of MacOS, Windows 10 Professional, or Linux, you need
Docker and Git:

* [Docker](https://www.docker.com/products/overview)
* [Git](https://git-scm.com/)

If you are not using a recent MacOS, Windows 10 Professional, or Linux, you'll
have need to use either Docker Toolbox, which is temperamental and not covered,
or run Docker in a Vagrant box, provided here:

* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Vagrant for Docker](https://github.com/JohnTasto/vagrant-for-docker)
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)

### Services Development Environment

##### Start:

Run Django and PostgreSQL:
```
$ docker-compose up
```

You can also run it in the background:
```
$ docker-compose up -d
```
It looks like it starts faster this way, but give it a bit to import data into
the database in the background before trying to view it in a browser.

##### Shutdown:

```
$ docker-compose down
  # or
$ docker-compose down --rmi all   # remove images to save disk space
```

##### Rebuild images (necessary if `requirements.txt` changes):

```
$ docker-compose down   # (if not already shut down)
$ docker-compose up --build
```

##### Container access examples:

Run manage.py command directly:

```
docker-compose exec web ./manage.py <command>
```

Run the Python shell:

```
docker-compose exec web ./manage.py shell
```

Run the PostgreSQL shell:

```
docker-compose exec --user postgres db psql
```

### Develop!

Have at it!

View the API GUI at localhost:8000.

Feel free to explore the [API docs](https://github.com/hackoregon/housing-17/tree/backend/docs/API.md).

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

See the DevOps page of the [Wiki](https://github.com/hackoregon/housing-17/wiki) for notes about how to deploy this on a live system

## Built With

See the [Wiki](https://github.com/hackoregon/housing-17/wiki) for notes about the front-end, datbases, and web framework used for the project

## Contributing

All Hack Oregon projects are open source, built entirely by volunteers from our local community. Visit [Hack Oregon - Build With Us](http://www.hackoregon.org/join/) to learn more!

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Core Team

* **Adrienne Tilley** - *Design Lead*
* **Bimal Rajbhandary** - *Domain Expert / Strategic Development*
* **Avi Lundberg** - *Design Lead*
* **David Daniel** - *Tech Lead*
* **Derek Demaria** - *Front-end Lead*
* **Gabriele Hayden** - *Facilitator / Strat Dev*
* **Victoria James** - *Domain Expert / Strategic Development*
* **Warren Friedland** - *Tech Lead*
* **Kartik Nagappa** - *Design Lead*
* **Riley Rustad** - *Tech Lead*

See also the list of [contributors](https://github.com/hackoregon/housing-17/contributors) who participated in this project.

## Acknowledgments

* [Crop Compass](http://www.cropcompass.org/)
* [PlotPDX](http://plotpdx.org)
* [Programming to Progress](http://www.programmingtoprogress.org/)
