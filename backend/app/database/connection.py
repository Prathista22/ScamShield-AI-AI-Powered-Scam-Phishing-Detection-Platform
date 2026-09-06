"""
MySQL connection helper — Member 2's module.

Reads credentials from environment variables so nobody commits passwords.
Create a `.env` file (already gitignored) alongside this project with:

    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=yourpassword
    DB_NAME=scamshield
"""
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "scamshield"),
    )
