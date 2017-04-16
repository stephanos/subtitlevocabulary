set -e

$(pwd)/scripts/build-container.sh

# remove Python cache first
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

docker run \
    --rm \
    --name check \
    -it \
    -v $(pwd):/app/src \
    stephanos/subvoc \
    /bin/bash -c "flake8 && \
                  pytest --cov --diff && sed -i \"s|/app/src/|`pwd`/|g\" .coverage && \
                  /opt/node_modules/eslint/bin/eslint.js static/js/app/**/*.es6 && \
                  /opt/node_modules/jest/bin/jest.js --runInBand"