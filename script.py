def generate_query(table_name, column_name, entries):
    query = f"SELECT * FROM SQL_EDITOR_{table_name}_TABLE \nWHERE "
    conditions = []

    for entry in entries:
        conditions.append(f"LOWER({column_name}) LIKE LOWER('%{entry}%')")

    query += " OR ".join(conditions) + ";"
    return query

def main():
    table_name = input("Enter the name of the table: ")
    column_name = input("Enter the name of the column for condition: ")

    entries = []
    print("Enter the list of entries (one entry per line). Type 'done' when finished:")
    while True:
        entry = input().strip()
        if entry.lower() == 'done':
            break
        entries.append(entry)

    query = generate_query(table_name, column_name, entries)
    print("Generated SQL query:")
    print(query)

if __name__ == "__main__":
    main()
