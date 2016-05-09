from flask import Flask, redirect, render_template
from datetime import datetime
import csv,random
app = Flask(__name__)


#creating csv file
with open('templates/eqdata.csv','wb') as fwrite:
    writer = csv.writer(fwrite)
    for i in range(1,10):
        writer.writerow((i,datetime.now().strftime("%Y-%m-%d"),
                         datetime.now().strftime('%H:%M:%S'),'apple','ball','cat',
                         random.uniform(4,8)))

@app.route('/')
def main():
    return render_template('eqMain.html')

@app.route('/index')
def tab1():
    return render_template('tab1_index.html')

@app.route('/eqhis')
def history():
    return render_template('tab2_eqhis.html')

@app.route('/eqrealdata')
def real():
    #reading the created csv file
    with open('templates/eqdata.csv', 'rb') as fread:
        reader = csv.reader(fread)
        dict={}
        for a in reader:
            dict[a[0]]=[ a[1], a[2], a[3], a[4], a[5],a[6]] 
            #publishing the values to web
        return render_template('tab3_eqrealdata.html', result=dict)

@app.route('/about')
def about():
    return render_template('tab4_about.html')
if __name__ == '__main__':
    app.run(debug=True)
