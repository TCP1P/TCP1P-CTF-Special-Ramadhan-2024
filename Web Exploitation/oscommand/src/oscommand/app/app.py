import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form['ip']
        blacklist = [';', '&', '|', '||', '&&', '>', '<', '(', ')', '{', '}', '[', ']', '\\', '\'', '"', '!', '*', '?', '~', '#', '%', '+', ' ']
        if any(x in ip for x in blacklist):
            result = 'wleee gabisa :p'
        else:
            result = os.popen(f'dig {ip}').readlines()
            result = '<br>'.join(result)
    else:
        result = None
    html = f''' 
    <html>
    <body>
    <p> dag DIG dug duarrr ... mercon daiya </p>
    <form action="/" method="post">
        <input type="text" name="ip" placeholder="google.com">
        <input type="submit" value="dig">
    </form>
    <h2> Result </h2>
    <p>Result: {result}</p>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)