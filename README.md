# Natural Language to SQL Query Generator using MySQL and Gemini AI

This project integrates the Gemini language model with a MySQL database schema to generate SQL queries from natural language inputs. The application first retrieves the database schema, formats it, and then sends the schema along with the user's query to the Gemini model to generate an appropriate SQL query.

## Features
- **MySQL Database Schema Retrieval**: Automatically retrieves and formats table and column details from the connected MySQL database.
- **Gemini Language Model**: Uses Gemini AI to interpret natural language queries and generate SQL statements based on the provided schema.
- **Simple and Modular Code**: Easily understandable, with clear function definitions for schema retrieval and SQL generation.

## Prerequisites
Before running the project, ensure you have the following:
- Python 3.8 or above
- API Key for Gemini AI
- MySQL database credentials (host, user, password, and database name)

## Setup

1. **Install Dependencies**:
   ```bash
   pip install mysql-connector-python google-generativeai
