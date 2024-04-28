from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Ruta para la página principal
@app.route('/')
def index():
    if 'username' in session:
        productos = [
            {"ID":"001","producto": "Monitor", "precio": 3500, "stock": 9},
            {"ID":"002","producto": "CPU", "precio": 6500, "stock": 22},
            {"ID":"003","producto": "MEMORIA RAM", "precio": 300, "stock": 32},
            {"ID":"004","producto": "SSD", "precio": 700, "stock": 99},
            {"ID":"005","producto": "M.2", "precio": 1200, "stock": 120}
        ]
        return render_template('index.html', productos=productos)
    return redirect(url_for('login'))

# Ruta para la página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))  # Redirige a index si ya ha iniciado sesión
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'root' and password == 'admin1':
            session['username'] = username
        if username == 'Emma' and password == 'admin1':
            session['username'] = username    
            return redirect(url_for('index'))  # Redirige a index si la autenticación es exitosa
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    return render_template('login.html', error=None)

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Ruta para login.html
@app.route('/login.html')
def login_html():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
