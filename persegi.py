
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Selamat datang di aplikasi Flask Rifka!"

@app.route("/nama/<nama>")
def nama(nama):
    return f"Halo, {nama}! Selamat belajar Flask."

@app.route("/umur/<int:usia>")
def umur(usia):
    return f"Umur kamu adalah {usia} tahun."

@app.route("/luas/<int:panjang>/<int:lebar>")
def luas(panjang, lebar):
    hasil = panjang * lebar
    return f"Luas persegi panjang adalah {hasil}."

@app.route("/angka/<int:n>")
def angka(n):
    if n % 2 == 0:
        return f"{n} adalah bilangan genap."
    else:
        return f"{n} adalah bilangan ganjil."

@app.route("/nilai/<int:nilai>")
def nilai(nilai):
    if nilai >= 75:
        return f"Nilai {nilai}: Kamu LULUS!"
    else:
        return f"Nilai {nilai}: Kamu TIDAK LULUS."

@app.route("/kali/<int:a>/<int:b>")
def kali(a, b):
    hasil = a * b
    return f"Hasil perkalian {a} x {b} = {hasil}"

@app.route("/name/<name>")
def pacar(name):
    return f"Halo, {name}! Selamat pagi cintakuuu."

if __name__ == "__main__":
    app.run(debug=True)
