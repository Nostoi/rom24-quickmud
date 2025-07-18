FROM python:3.11-slim

# Build steps start in /app so we can copy the whole repository
WORKDIR /app

# Copy project metadata first for better layer caching
COPY mud/pyproject.toml mud/pyproject.toml

# Copy the mud package including a lock file if present
COPY mud/ mud/

# Install Poetry and project dependencies. If no lock file is present,
# generate one during the build.
RUN pip install --no-cache-dir poetry \
    && if [ ! -f mud/poetry.lock ]; then \
         poetry -C mud lock; \
       fi \
    && poetry -C mud install --no-interaction --no-ansi

# Copy the rest of the repository
COPY . .

# The application expects to run from the mud directory where
# pyproject.toml lives so Poetry can locate the project
WORKDIR /app/mud

CMD ["poetry", "run", "mud", "socketserver"]
