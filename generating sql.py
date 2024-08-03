def generate_sql(nl_query):
    # Format the prompt with schema and natural language query
    input_text = f"""
    Database Schema:
    {schema_details}
    
    Natural Language Query: {nl_query}

    Output:
    SQL Query:
    """

    print(input_text)
    response = chat_session.send_message(input_text)
    return response.text.strip()

# Example usage
nl_query = "natural language query"
sql_query = generate_sql(nl_query)
print(f"Generated SQL: {sql_query}")

# Close the database connection
db_connection.close()
