from flask import Flask, request, render_template
from lxml import etree

app = Flask(__name__)

# Load XML data
tree = etree.parse('users.xml')
root = tree.getroot()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['GET'])
def query():
    name = request.args.get('name', '')
    xpath_query = f"/users/user[username='{name}']"
    result = root.xpath(xpath_query)

    if len(result) > 0:
        return f"User {etree.tostring(result[0], encoding=str)} found!"
    else:
        return "No matching user found."


if __name__ == '__main__':
    app.run(debug=True)
