from cs50 import SQL

# Conectar a la base de datos
db = SQL("sqlite:///users.db")

# Limpiar tablas existentes
tables = ["user_responses", "user_trivias", "responses", "questions", "trivias", "categories"]
for table in tables:
    db.execute(f"DELETE FROM {table};")

# Insertar categorías
db.execute("""
    INSERT INTO categories (category_id, name) VALUES
    (1, 'Cultura General'),
    (2, 'Historia'),
    (3, 'Gastronomía'),
    (4, 'Arte'),
    (5, 'Tradiciones');
""")

# Insertar trivias
db.execute("""
    INSERT INTO trivias (trivia_id, user_id, category_id, title, image, points) VALUES
    (1, NULL, 1, 'Símbolos Nacionales de Nicaragua', '/static/Simbolos_nacionales.jpg', 10),
    (2, NULL, 2, 'Historia de Nicaragua', '/static/historia.jpg', 15),
    (3, NULL, 3, 'Gastronomía Nicaragüense', '/static/gastronomia.jpg', 20),
    (4, NULL, 4, 'Literatura Nicaragüense', '/static/literatura.jpg', 25),
    (5, NULL, 5, 'Leyendas de Nicaragua', '/static/leyendas.jpg', 30);
""")

# Insertar preguntas y respuestas para Trivia 1: Símbolos Nacionales de Nicaragua
db.execute("""
    INSERT INTO questions (question_id, trivia_id, question_text) VALUES
    (1, 1, '¿Cuál es el símbolo nacional de Nicaragua que aparece en el centro de la bandera?'),
    (2, 1, '¿Qué representan los cinco volcanes en el escudo de armas de Nicaragua?'),
    (3, 1, '¿Cuál es la flor nacional de Nicaragua?');
""")

db.execute("""
    INSERT INTO responses (response_id, question_id, trivia_id, response_text, correct) VALUES
    (1, 1, 1, 'Un triángulo equilátero', 1),
    (2, 1, 1, 'Un rectángulo azul', 0),
    (3, 1, 1, 'Un círculo dorado', 0),
    (4, 2, 1, 'Los cinco países de Centroamérica', 1),
    (5, 2, 1, 'Las cinco montañas más altas', 0),
    (6, 2, 1, 'Las cinco luchas por la independencia', 0),
    (7, 3, 1, 'Sacuanjoche', 1),
    (8, 3, 1, 'Flor de Mayo', 0),
    (9, 3, 1, 'Jazmín', 0);
""")

# Insertar preguntas y respuestas para Trivia 2: Historia de Nicaragua
db.execute("""
    INSERT INTO questions (question_id, trivia_id, question_text) VALUES
    (4, 2, '¿En qué año se independizó Nicaragua de España?'),
    (5, 2, '¿Qué conflicto armado ocurrió en Nicaragua entre 1981 y 1990?'),
    (6, 2, '¿Quién fue el líder del Frente Sandinista de Liberación Nacional (FSLN) que llegó al poder en 1979?');
""")

db.execute("""
    INSERT INTO responses (response_id, question_id, trivia_id, response_text, correct) VALUES
    (10, 4, 2, '1821', 1),
    (11, 4, 2, '1905', 0),
    (12, 4, 2, '1838', 0),
    (13, 5, 2, 'La Guerra de los Contras', 1),
    (14, 5, 2, 'La Revolución Liberal', 0),
    (15, 5, 2, 'La Guerra Fría', 0),
    (16, 6, 2, 'Daniel Ortega', 1),
    (17, 6, 2, 'Anastasio Somoza', 0),
    (18, 6, 2, 'Violeta Barrios', 0);
""")

# Insertar preguntas y respuestas para Trivia 3: Gastronomía Nicaragüense
db.execute("""
    INSERT INTO questions (question_id, trivia_id, question_text) VALUES
    (7, 3, '¿Cuál es el plato nacional de Nicaragua?'),
    (8, 3, '¿Qué bebida tradicional se elabora con maíz fermentado?'),
    (9, 3, '¿Qué dulce típico es originario de León?');
""")

db.execute("""
    INSERT INTO responses (response_id, question_id, trivia_id, response_text, correct) VALUES
    (19, 7, 3, 'Gallo Pinto', 1),
    (20, 7, 3, 'Baho', 0),
    (21, 7, 3, 'Vigorón', 0),
    (22, 8, 3, 'Chicha', 1),
    (23, 8, 3, 'Pinolillo', 0),
    (24, 8, 3, 'Cacao', 0),
    (25, 9, 3, 'Cajeta de leche', 1),
    (26, 9, 3, 'Rosquillas', 0),
    (27, 9, 3, 'Turrón', 0);
""")

# Insertar preguntas y respuestas para Trivia 4: Literatura Nicaragüense
db.execute("""
    INSERT INTO questions (question_id, trivia_id, question_text) VALUES
    (10, 4, '¿Quién es considerado el poeta más importante de Nicaragua?'),
    (11, 4, '¿En qué año Rubén Darío publicó *Azul*?'),
    (12, 4, '¿Qué corriente literaria es asociada con Rubén Darío?');
""")

db.execute("""
    INSERT INTO responses (response_id, question_id, trivia_id, response_text, correct) VALUES
    (28, 10, 4, 'Rubén Darío', 1),
    (29, 10, 4, 'Ernesto Cardenal', 0),
    (30, 10, 4, 'Salomón de la Selva', 0),
    (31, 11, 4, '1888', 1),
    (32, 11, 4, '1890', 0),
    (33, 11, 4, '1875', 0),
    (34, 12, 4, 'Modernismo', 1),
    (35, 12, 4, 'Romanticismo', 0),
    (36, 12, 4, 'Realismo', 0);
""")

# Insertar preguntas y respuestas para Trivia 5: Leyendas de Nicaragua
db.execute("""
    INSERT INTO questions (question_id, trivia_id, question_text) VALUES
    (13, 5, '¿Cuál es la leyenda que habla de un espíritu femenino en busca de sus hijos?'),
    (14, 5, '¿Qué leyenda narra sobre una carreta espectral que aparece de noche?'),
    (15, 5, '¿Qué figura mítica protege a los borrachos de la región?');
""")

db.execute("""
    INSERT INTO responses (response_id, question_id, trivia_id, response_text, correct) VALUES
    (37, 13, 5, 'La Llorona', 1),
    (38, 13, 5, 'La Cegua', 0),
    (39, 13, 5, 'La Carreta Nagua', 0),
    (40, 14, 5, 'La Carreta Nagua', 1),
    (41, 14, 5, 'El Cadejo', 0),
    (42, 14, 5, 'La Mocuana', 0),
    (43, 15, 5, 'El Cadejo', 1),
    (44, 15, 5, 'La Cegua', 0),
    (45, 15, 5, 'La Llorona', 0);
""")

print("Datos insertados correctamente.")
