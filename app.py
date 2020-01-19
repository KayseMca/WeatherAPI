# using weather API creating flask App
from flask import Flask, flash,redirect,request, url_for, render_template,jsonify
from weather import query_api
#from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
     data=[
         {'name':'Toronto'}, 
         {'name':'Montreal'}, 
         {'name':'Calgary'}, 
         {'name':'Ottawa'}, 
         {'name':'Edmonton'}, 
         {'name':'Mississauga'},        
         {'name':'Winnipeg'}, 
         {'name':'Vancouver'}, 
         {'name':'Brampton'},
         {'name':'Quebec'},
         {'name':'Hargeysa'},
         {'name':'Ankara'},
         {'name':'Mogadishu'},
         {'name':'Sakarya'},
         {'name':'Boosaaso'}
         ]
    
     return render_template('weather.html',data=data)


@app.route('/result', methods=['GET','POST'])
def result():
    data =[]
    error = None
    select = request.form.get('data')
    resp = query_api(select)
    
    if resp:
        data.append(resp)
        if len(data)!=2:
            error = 'Bad Response from Weather API'
        
    #return jsonify(data)

    return render_template('result.html',data=data,error=error)


if __name__=='__main__':
    app.run(port=5000, debug=True)


