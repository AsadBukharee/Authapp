@echo off
setlocal enabledelayedexpansion

REM Log file path
set LOG_FILE=%~dp0init_pg_db_win.log

REM Load environment variables from .env.dev
for /f "usebackq tokens=1,2 delims==" %%A in ("..\env\.env.dev") do (
    set %%A=%%B
)

REM Check if environment variables are set
if not defined DB_NAME (
    echo ERROR: DB_NAME is not set. Check your .env.dev file. >> "%LOG_FILE%"
    exit /b 1
)
if not defined DB_USER (
    echo ERROR: DB_USER is not set. Check your .env.dev file. >> "%LOG_FILE%"
    exit /b 1
)
if not defined DB_PASSWORD (
    echo ERROR: DB_PASSWORD is not set. Check your .env.dev file. >> "%LOG_FILE%"
    exit /b 1
)
if not defined DB_HOST (
    echo ERROR: DB_HOST is not set. Check your .env.dev file. >> "%LOG_FILE%"
    exit /b 1
)
if not defined DB_PORT (
    echo ERROR: DB_PORT is not set. Check your .env.dev file. >> "%LOG_FILE%"
    exit /b 1
)

REM Create database
echo Creating database %DB_NAME%...

REM Command to create database
psql -U %DB_USER% -h %DB_HOST% -p %DB_PORT% -c "CREATE DATABASE %DB_NAME%;" >> "%LOG_FILE%" 2>&1

if %ERRORLEVEL% neq 0 (
    echo Failed to create the database. Check the log file at %LOG_FILE%.
    exit /b %ERRORLEVEL%
) else (
    echo Database %DB_NAME% created successfully.
)

endlocal
