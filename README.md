# Data Sources Branch
This branch is used for version control and review of CSVs derived from the variety of data sources used by the Housing Team. See the [Data Sources Wiki Page] (https://github.com/hackoregon/housing-17/wiki/Data-Sources) for more information.

Note that because this branch should not be merged with the integration branch `master` - see the [DevOps wiki] (https://github.com/hackoregon/housing-17/wiki/DevOps) for more information on deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
```
# From your local machine, set up Git
# From GitHub, set up GitHub Authentication
# From GitHub, fork the Repo at `https://github.com/hackoregon/housing-17`

# Clone the GitHub repository using SSH or HTTPS
$ git clone git@github.com:YOUR-USERNAME/housing-17.git
# or...
$ git clone https://github.com/YOUR-USERNAME/housing-17.git

# Refresh
$ git pull origin master

# Check out the datasources branch
$ git checkout datasources

# Add or update files
$ git add -A

# Commit the changes
$ git commit -m "my changes"

# Push changes to the new feature branch
$ git push origin datasources

# To initiate a merge of your new feature, from GitHub choose Pull Request

```
