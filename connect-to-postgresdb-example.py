import psycopg2

engine = psycopg2.connect(f"""host={db_host} port={db_port} dbname={db_name} user={db_user} password={db_password} options = '-c search_path={db_search_path}'""")
