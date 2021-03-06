from flask import Flask, render_template, request,redirect
from instamojo_wrapper import Instamojo

API_KEY = "####yourapikey####"

AUTH_TOKEN = "####yourauthtoken####"

api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/pay',methods=['POST','GET'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name')
        purpose = request.form.get('purpose')
        email = request.form.get('email')
        amount = request.form.get('amount')
        
        response = api.payment_request_create(
        amount=amount,
        purpose=purpose,
        buyer_name=name,
        send_email=True,
        email=email,
        redirect_url="http://localhost:5000/success"
        )
        
        return redirect(response['payment_request']['longurl'])
    
    else:
        
        return redirect('/')

    
if __name__ == '__main__':
   app.run(debug=True)