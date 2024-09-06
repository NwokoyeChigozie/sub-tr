

FROM python:3.11.9-alpine3.20

WORKDIR /app
# vibrant-data-labs-py2mappr


# Copy requirements file and install dependencies
COPY _requirements.txt ./
RUN pip install --no-cache-dir -r _requirements.txt

# Copy the rest of the application code
COPY . .

RUN pytest


WORKDIR /
RUN apk update && apk add bash
COPY run_tests.sh ./
RUN chmod +x /run_tests.sh
ENTRYPOINT ["/bin/bash", "-s"]