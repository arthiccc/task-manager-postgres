#!/bin/bash

echo "Setting up Task Manager Database..."

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo ".env file not found. Please create one from .env.example"
    exit 1
fi

# Create database if it doesn't exist
echo "Creating database..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || \
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -c "CREATE DATABASE $DB_NAME"

# Run schema
echo "Creating tables..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f db/schema.sql

# Run seed data
echo "Inserting seed data..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f db/seed.sql

echo "Setup complete! Run 'python scripts/run.py' to start the application."
