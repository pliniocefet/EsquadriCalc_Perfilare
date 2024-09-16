import sqlite3

# Database connection
def connect_db():
    return sqlite3.connect('esquadriaDB.db')

# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Create operation
def create_user(usuario, senha):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO usuarios (usuario, senha)
    VALUES (?, ?)
    ''', (usuario, senha))
    conn.commit()
    conn.close()

# Read operation
def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update operation
def update_user(id, usuario, senha):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE usuarios
    SET usuario = ?, senha = ?
    WHERE id = ?
    ''', (usuario, senha, id))
    conn.commit()
    conn.close()

# Delete operation
def delete_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = ?''', (id,))
    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    create_table()
    
    # Create
    create_user("plinio", "123")
    
    # Read
    usuario = read_users()
    print("Usuario Criado:")
    for user in usuario:
        print(user)
    
    # Update
    #update_user(1, "plinio correa", "123")
    
    # Read again
    #usuarios = read_users()
    #print("Usuarios Atualizados:")
    #for user in usuarios:
    #    print(user)
    
    # Delete
    #delete_user(2)
    
    # Read again
    #usuario = read_users()
    #print("Usuario Apagado:")
    #for user in usuario:
    #    print(user)
