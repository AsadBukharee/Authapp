#!/bin/bash

# Load environment variables from .env.dev
set -a
source ../env/.env.dev
set +a

# Log file path
LOG_FILE="$(dirname "$0")/init_pg_db_lnx.log"

# Validate necessary environment variables
if [ -z "$DB_NAME" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ] || [ -z "$DB_HOST" ] || [ -z "$DB_PORT" ]; then
  echo "One or more environment variables are missing. Please check your .env.dev file." | tee -a "$LOG_FILE"
  exit 1
fi

# Create the database
echo "Creating database $DB_NAME..." | tee -a "$LOG_FILE"

# Command to create database
PGPASSWORD="$DB_PASSWORD" psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -c "CREATE DATABASE $DB_NAME;" >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Failed to create the database. Check the log file at $LOG_FILE." | tee -a "$LOG_FILE"
    exit 1
else
    echo "Database $DB_NAME created successfully." | tee -a "$LOG_FILE"
fi
