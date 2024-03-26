from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    account = open("account.txt", "r").read().splitlines()
    username = account[0].split(":")[0]
    password = account[0].split(":")[1]
    otp = account[0].split(":")[-1]
    html = '''
    <h3> sorry web nya burik 😭😭😭 </h3>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
        </form>
        
        <a href="/reset">Reset Password</a>
    '''
    if request.method == "POST":
        if request.form["username"] == username and request.form["password"] == password:
            return "TCP1P{acc0unt_takeover_so_ez_witout_rate_limit}"
        else:
            return "Invalid username or password"
    return html

@app.route("/reset", methods=["GET", "POST"])
def reset():
    account = open("account.txt", "r").read().splitlines()
    username = account[0].split(":")[0]
    password = account[0].split(":")[1]
    otp = account[0].split(":")[-1]
    html = '''
    <form method="POST">
        <input type="text" name="username" placeholder="username" required>
        <button type="submit">Reset Password</button>
        </form>
    '''
    if request.method == "POST":
        if request.form["username"] == username:
            otphtml = f'''
            <form method="POST">
                <input type="hidden" name="username" value="{request.form["username"]}">
                <input type="text" name="otp" placeholder="4 digit OTP" required>
                <input type="password" name="newpassword" placeholder="New Password" required>
                <button type="submit">Reset Password</button>
                </form>
            '''
            if "otp" in request.form:
                print(request.form["otp"] == otp)
                if request.form["otp"] == otp:
                    import random
                    otp = str(random.randint(0, 999)).zfill(4)
                    account = f"{username}:{request.form['newpassword']}:{otp}"
                    open("account.txt", "w").write(account)
                    return "changed successfully! Please login again <br> <a href='/'>Login</a>"
                else:
                    return "Invalid OTP"
            else:
                return otphtml
        else:
            return "account doesn't exist!"
    return html

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')