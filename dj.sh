function usage {
  echo "usage:"
  echo "  $ ./dj.sh up                start Docker and run Django API"
  echo "     --build                  rebuild all images (ie, if requirments.txt changes)"
  echo "  $ ./dj.sh down              shut down Docker and Django API"
  echo "     --rmi                    remove images to save disk space"
  echo "  $ ./dj.sh manage <command>  run manage.py command directly"
}

function importData {
  echo "Migrating database..."
  while ! docker-compose exec web ./manage.py migrate >> /dev/null ; do
    sleep 1
  done
  echo "Loading data..."
  docker-compose exec web ./manage.py shell --command="import housing_backend.loader"
}

case $1 in
  up )
    if [ "$2" == '--build' ]; then
      docker-compose up --build -d
    else
      docker-compose up -d
    fi
    importData
    exit
    ;;
  down )
    if [ "$2" == '--rmi' ]; then
      docker-compose down --rmi all
    else
      docker-compose down
    fi
    exit
    ;;
  manage )
    shift
    docker-compose exec web ./manage.py "$@"
    ;;
  * )
    usage
    exit 1
esac
