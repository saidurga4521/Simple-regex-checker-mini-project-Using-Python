from flask import Flask,request,render_template
import re

app=Flask(__name__)

#now create the regex checker

@app.route('/regex_page',methods=['POST','GET'])

def index():
    if request.method=='POST':
        test_string=request.form['test_string']
        regex=request.form['regex']
        matches=re.findall(regex,test_string)
        return render_template('index.html',test_string=test_string,regex=regex,matches=matches)
    else:
        return render_template('index.html')
    
    
#run the code

if __name__=='__main__':
    app.run(debug=True)