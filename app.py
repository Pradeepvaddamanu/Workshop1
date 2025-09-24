from flask import Flask
app= Flask(__name__)
#Pradeep
@app.route('/')
def hello_world():
    a = "pradeep"
    return 'Hello from Flask' + a

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')
