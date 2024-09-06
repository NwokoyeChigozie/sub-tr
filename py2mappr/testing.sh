# Create a script in local to run in container
cat >  ~/test.sh<< EOF
#!/bin/bash   
echo "Hello from external script!"             
set -euo pipefail

/run_tests.sh
EOF



# Trigger run_tests.sh in docker container from local.
docker run --platform linux/amd64 -i vibrant-data-labs-py2mappr:latest < ~/test.sh

# docker save vibrant-data-labs-py2mappr:latest > /Users/greg/turing/py2mappr/vibrant-data-labs-py2mappr.tar