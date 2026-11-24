from flask import Flask, render_template, request

app = Flask(__name__)


# Halaman utama: GET menampilkan form, POST memproses isi form
@app.route("/", methods=["GET", "POST"])
def index():
    nama = ""
    hasil = ""

    if request.method == "POST":
        # Mengambil isi textfield yang atribut name-nya "nama"
        nama = request.form.get("nama", "").strip()

        if nama == "":
            hasil = "Nama tidak boleh kosong!"
        else:
            hasil = f"Halo, {nama}!"

    return render_template("index.html", nama=nama, hasil=hasil)


@app.route("/about")
def about():
    return "About us"


@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"


@app.route("/post/<int:post_id>")
def post(post_id):
    post_id = post_id + 15
    return f"Post #{post_id}"


@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"


@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"


if __name__ == "__main__":
    app.run(debug=True)