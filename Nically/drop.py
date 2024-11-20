from cs50 import SQL

# Conectar a la base de datos
db = SQL("sqlite:///users.db")

# Dropear todas las tablas existentes
db.execute("DROP TABLE IF EXISTS user_responses;")
db.execute("DROP TABLE IF EXISTS user_trivias;")
db.execute("DROP TABLE IF EXISTS responses_correct;")
db.execute("DROP TABLE IF EXISTS responses;")
db.execute("DROP TABLE IF EXISTS questions;")
db.execute("DROP TABLE IF EXISTS trivias;")
db.execute("DROP TABLE IF EXISTS categories;")

print("Todas las tablas han sido eliminadas.")
