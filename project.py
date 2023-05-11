from flask import Flask, app, jsonify, request

app=Flask(__name__)


contacts= [
    {
        "Contact": "9987644456",
        "Name": "Raju",
        "done":False,
        "id":1
    },
    {
        "Contact": "9876543222",
        "Name":"Rahul",
        "done":False,
        "id":2
    },
   

]

@ app.route('/')
def home():
    return "Welcome to the home page. Let's take a look at some contacts."

@app.route('/sendinfo', methods=['POST'])
def sendinfo():
    if not request.json:
        return jsonify({'status':'Error', 'Message':'Invalid Data'}, 400)
    temp = {
        'id': contacts[-1]['id'] + 1,
        'Contact': request.json['Contact'],
    }
    contacts.append(temp)
    return jsonify({'status':'Success', 'Message':'Data Added'}, 201)

@app.route('/getinfo', methods=['GET'])
def getinfo():
    return jsonify({'data': contacts})


if __name__ == '__main__':
    app.run(debug=True)