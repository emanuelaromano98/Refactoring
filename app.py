import base64
from io import BytesIO
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def plot():
    with open('plot.html', 'r') as f:
        plot_html = f.read()

    return render_template_string(plot_html)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5001, debug=True)
