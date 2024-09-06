# Create a script in local to run in container
cat >  ~/test.sh<< EOF
#!/bin/bash   
echo "Hello from external script!"             
set -euo pipefail

/run_tests.sh
EOF



# Trigger run_tests.sh in docker container from local.
docker run --platform linux/amd64 -i typoscript:latest < ~/test.sh

# docker save typoscript:latest > /Users/greg/turing/typoscript/typoscript.tar