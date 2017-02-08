# housing-17 
(a template for a README.md follows...)

# Project Title

Our goal is to create a tool that allows the public to easily understand and explore the state of housing in Portland.

### Requirements

* Python 3.5
* Django 1.10

### Installing

1. Clone the repository from the command line with:
```git clone git@github.com:hackoregon/housing-17.git```
2. Start a new python virtual environment:
```
virtualenv venv
```
3. Activate your new environment
```
source venv/bin/activate
```
3. Install necessary Python Libraries
```pip install -r requirements.txt```
4. Navigate to project directory and make database migrations.
```
cd backend
./manage migrate
```
5. Load data into database from csv file.
#TODO: where to pull data from?
#TODO: script that will load data into database for you?
6. Run the development server
```
./manage runserver
```
7. Have at it! Feel free to explore the [API docs](#)
#TODO: write API Docs

##### When you're done:
 1. Press ```ctrl + c``` to kill the dev server
 2. Enter ```deactivate``` at the command line to deactivate your virtual environments.
##### When you want to reactivate from the housing-17 directory:
```
source venv/bin/activate
cd backend
./manage runserver
```

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

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
