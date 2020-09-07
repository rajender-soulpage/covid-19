from flask import Flask
from flask import request, redirect, render_template, send_file
from score import *
 
from flask import Flask 
  
app = Flask(__name__) 

@app.route('/')
def index():
    '''
        base route
    '''
    return redirect('/covid.India.ai')

#starting page age.
@app.route('/covid.India.ai')
def page1():
    '''
        Page1
    '''
    return render_template('index.html')

#page2
@app.route('/covid.India.ai/Gender',methods = ['POST','GET'])
def Page2():
    '''
        Page2
    '''
    res1 = 0
    if(request.method == "POST"):
        res1=request.form['Age']

        if(len(user_input)==0):
            user_input.append(res1)
        else:
            user_input[0] = res1
    return render_template('gender.html')

#page4
@app.route('/covid.India.ai/common_sym',methods = ['POST','GET'])
def Page4():
    '''
        Page4
    '''
    res1 = 0
    if(request.method == "POST"):
        
        res1=request.form.to_dict()['answer']
        if(len(user_input)==1):
            user_input.append(res1)
        else:
            user_input[1] = res1
    return render_template('common_sym.html')


#page5
@app.route('/covid.India.ai/less_common_sym',methods = ['POST','GET'])
def Page5():
    '''
        Page5
    '''
    res1 = 0
    if(request.method == "POST"):

        res1=[symptom for symptom in request.form.to_dict().values()]
    
        if(len(user_input)==2):
            user_input.append(res1)
        else:
            user_input[2] = res1
    return render_template("less_common_sym.html")

#page6
@app.route('/covid.India.ai/Serious_sym',methods = ['POST','GET'])
def Page6():
    '''
        Page6
    '''
    res1 = 0
    if(request.method == "POST"):
        
        res1=[symptom for symptom in request.form.to_dict().values()]
        
        if(len(user_input)==3):
            user_input.append(res1)
        else:
            user_input[3] = res1
    return render_template("Serious_symptoms.html")

#page8
@app.route('/covid.India.ai/pre_existing_health',methods = ['POST','GET'])
def Page8():
    '''
        Page8
    '''
    res1 =0
    if(request.method == "POST"):
    
        res1=[symptom for symptom in request.form.to_dict().values()]
        
        if(len(user_input)==4):
            user_input.append(res1)
        else:
            user_input[4] = res1
    return render_template("pre_existing_health.html")

#page8
@app.route('/covid.India.ai/pre_existing_health2',methods = ['POST','GET'])
def Page10():
    '''
        Page8
    '''
    res1 =0
    if(request.method == "POST"):
        
        res1=[symptom for symptom in request.form.to_dict().values()]
        
        if(len(user_input)==5):
            user_input.append(res1)
        else:
            user_input[5] = res1
    return render_template("pre_existing_health2.html")

#page9
@app.route('/covid.India.ai/Result',methods = ['POST','GET'])
def page9():
    '''
        Page8
    '''
    res1 = 0
    if(request.method == "POST"):

        res1=[symptom for symptom in request.form.to_dict().values()]
        
        if(len(user_input)==6):
            user_input.append(res1)
        else:
            user_input[6] = res1
        score=get_score()
        print("\n the final sore :- ",score)
    return render_template("Result.html",value = score)

#running the main function.
if __name__ == '__main__':
    app.run(debug=False,use_reloader=False)