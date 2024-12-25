from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nama = request.form['nama']
        alamat = request.form['alamat']
        nim = request.form['nim']
        return f"Data berhasil dikirim!<br>Nama: {nama}<br>Alamat: {alamat}<br>NIM: {nim}"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
