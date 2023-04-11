#cmd >> pip install flask

from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "super secret key"

# Kullanıcının giriş yapmış olup olmadığını kontrol etmek için bir decorator oluşturuyoruz
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Anasayfa için route
@app.route('/')
@login_required
def home():
    return render_template('home.html')

# Giriş sayfası için route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

# Çıkış için route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
