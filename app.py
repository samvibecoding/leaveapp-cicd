from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>LeaveApp</title>
<h1>Employee Leave Request</h1>
<form method="post">
  <label>Name:</label>
  <input name="name" required><br><br>
  <label>Leave days:</label>
  <input name="days" type="number" min="1" max="30" required><br><br>
  <button type="submit">Submit</button>
</form>
{% if message %}<p><strong>{{ message }}</strong></p>{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None
    if request.method == 'POST':
        name = request.form['name'].strip()
        days = int(request.form['days'])
        message = f"Leave request received for {name}: {days} day(s)."
    return render_template_string(PAGE, message=message)

@app.route('/health')
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

