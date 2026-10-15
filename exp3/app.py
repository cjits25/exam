from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (replace with a database in production)
users = []

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        users.append({'username': username, 'email': email})
        return redirect(url_for('success'))
    
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)