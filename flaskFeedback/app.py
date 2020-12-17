from flask import Flask, render_template, request

app = Flask(__name__)

ENV = ' dev'

if ENV == 'dev':
  app.debug = True
  # set db here 
else:
  app.debug = True
  # set db here



@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    customer = request.form['customer']
    dealer = request.form['dealer']
    rating = request.form['rating']
    comments = request.form['comments']
    # print(customer, dealer, rating, comments)
    if customer == '' or dealer == '': 
      return render_template('index.html', message='Please enter required field')
    
    return render_template('success.html')


if __name__ == '__main__':
  app.run()