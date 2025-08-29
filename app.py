# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Calculator</title></head>
<body>
  <h2>Basic Calculator by Priyanshu</h2>
  <form method="post">
    <input type="number" name="a" required>
    <select name="op">
      <option value="add">+</option>
      <option value="sub">-</option>
    </select>
    <input type="number" name="b" required>
    <button type="submit">Calculate</button>
  </form>
  {% if result is not none %}
    <h3>Result: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calc():
    result = None
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        op = request.form["op"]
        result = a + b if op == "add" else a - b
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
