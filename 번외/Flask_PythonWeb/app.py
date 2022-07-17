from firebase import firebase
from flask import Flask, redirect, request, url_for, render_template
import crypto
import sys
sys.modules['Crypto'] = crypto

# config
# server will reload on source changes, and provide a debugger for errors
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)  # consume the configuration above

firebase = \
    firebase.FirebaseApplication(
        'https://python-c9cc6-default-rtdb.firebaseio.com/', None)


@app.route('/')
def index():
    result = firebase.get('/messages', None)
    test_dict = {}
    for key in reversed(result):
        test_dict[key] = result[key]
    return render_template('index.html', messages=test_dict)

# decorator which tells flask what url triggers this fn


@app.route('/messages')
def messages():
    result = firebase.get('/messages', None)
    test_dict = {}
    for key in reversed(result):
        test_dict[key] = result[key]
    return render_template('index.html', messages=test_dict)


@app.route('/about/<string:id>')
def about(id):
    result = firebase.get(f'/project/{id}', None)
    if result:
        if id == 'jin':
            return render_template('about.html', messages=result)
        else:
            return render_template('about2.html', messages=result)
    else:
        if id == 'jin':
            return render_template('about.html')
        else:
            return render_template('about2.html')


@app.route('/submit_message', methods=['POST'])
def submit_message():
    message = {
        'body': request.form['message'],
        'who': request.form['who']
    }
    firebase.post('/messages', message)
    return redirect(url_for('index'))


@app.route('/edit/<string:id>')
def edit(id):
    return render_template('add.html', user_id=id)


@app.route('/add', methods=['GET', 'POST'])
def send():
    #    mydb = db_conn.Database()

    if request.method == 'POST':
        user_id = request.form['user_id']
        date = request.form['date']
        description = request.form['description']
        link = request.form['link']

        project_message = {
            'user_id': user_id,
            'date': date,
            'description': description,
            'link': link
        }
        firebase.post(f'/project/{user_id}', project_message)

    #   mydb.cursor.execute('''INSERTid INTO contacts(name, email, message) VALUES  ('{}', '{}', '{}')'''.format(name, email, message))
    #   mydb.db.commit()

        print(date, description, link, id)
        return redirect(url_for('about', id=user_id))

# key =


@app.route('/delete', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        link = request.form['_delete']
        user_id = request.form['user_id']

    data = firebase.get(f'/project/{user_id}/', None)
    print(data)
    for d in data:
        data_inner = firebase.get(f'/project/{user_id}/{d}/', None)
        print(data_inner['link'])
        if data_inner['link'] == link:
            key = d
            break
    print(key)
    firebase.delete(f'/project/{user_id}/', key)

    return redirect(url_for('about', id=user_id))


if __name__ == "__main__":
    app.run()
