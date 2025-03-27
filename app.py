from flask import Flask,render_template,send_file,request,redirect,url_for
app=Flask(__name__)
from sdmail import sendmail
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/mail')
def mail():
    return 'mail sended successfully'
@app.route('/resume')
def resume():
    pdf_file='./Srinu_Full_Stack_Developer.pdf'
    return send_file(pdf_file, as_attachment=True)
@app.route('/project-1')
def project1():
    return render_template('project-1.html')
@app.route('/project-2')
def project2():
    return render_template('project-2.html')
@app.route('/project-3')
def project3():
    return render_template('project-3.html')
@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        subject=name
        body=message
        sendmail(From=email,subject=subject,body=body)
        return redirect(url_for('mail'))
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,use_reloader=True)
