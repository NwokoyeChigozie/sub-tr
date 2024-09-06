# Create a script in local to run in container
cat >  ~/test.sh<< EOF
#!/bin/bash   
echo "Hello from external script!"             
set -euo pipefail

/run_tests.sh
EOF



# Trigger run_tests.sh in docker container from local.
docker run --platform linux/amd64 -i heroku-logger:latest < ~/test.sh

docker save heroku-logger:latest > /Users/greg/turing/heroku-logger/heroku-logger.tar