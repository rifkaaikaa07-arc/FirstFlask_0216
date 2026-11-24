from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nama = ""
    umur = ""
    nim = ""
    hasil = ""
    sukses = True

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        umur = request.form.get("umur", "").strip()
        nim = request.form.get("nim", "").strip()

        if nama == "" or umur == "" or nim == "":
            hasil = "Semua data harus diisi!"
            sukses = False
        elif not umur.isdigit() or not (1 <= int(umur) <= 80):
            hasil = "Umur harus berupa angka 1 - 80!"
            sukses = False
        elif not nim.isdigit():
            hasil = "NIM harus berupa angka!"
            sukses = False
        else:
            hasil = f"Halo, {nama}! Umur {umur} tahun, NIM {nim}."

    return render_template(
        "index.html",
        nama=nama, umur=umur, nim=nim, hasil=hasil, sukses=sukses
    )


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