from math import nextafter
from flask import Flask, redirect, url_for, request, render_template, flash
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about/<string:id>')
def about(id):
    if id == 'jin':
        return render_template('about.html')
    else:
        return render_template('about2.html')

@app.route('/add')
def add():
    print(request.url)
    return render_template('add.html', next_url=request.url)

@app.route('/add/<string:user_id>', methods=['GET', 'POST'])
def send(user_id):
#    mydb = db_conn.Database()
   
   if request.method == 'POST':
      url_id = user_id
      date = request.form['date']
      description = request.form['description']
      link = request.form['link']

    #   mydb.cursor.execute('''INSERT INTO contacts(name, email, message) VALUES  ('{}', '{}', '{}')'''.format(name, email, message))
    #   mydb.db.commit()
      print(date, description, link, url_id)
      return redirect(url_for('about', id =url_id))

if __name__ == '__main__':
   app.run(debug = True)
