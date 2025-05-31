from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Hitung Umur</title></head>
<body>
    <h2>Hitung Umur Siswa</h2>
    <form method="post">
        Nama: <input type="text" name="nama"><br>
        Tahun Lahir: <input type="text" name="tahun"><br>
        <input type="submit" value="Hitung">
    </form>
    {% if hasil %}
        <p>{{ hasil }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        nama = request.form["nama"]
        try:
            tahun_lahir = int(request.form["tahun"])
            umur = datetime.now().year - tahun_lahir
            hasil = f"Halo {nama}, umur kamu adalah {umur} tahun."
        except ValueError:
            hasil = "Tahun lahir harus berupa angka!"
    return render_template_string(HTML, hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
