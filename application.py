from flask import Flask,render_template,send_file,request,redirect,url_for
application=Flask(__name__)
from sdmail import sendmail
@application.route('/')
def index():
    return render_template('index.html')
@application.route('/mail')
def mail():
    return 'mail sended successfully'
@application.route('/resume')
def resume():
    pdf_file='./Srinivasarao_Ch_Resume.pdf'
    return send_file(pdf_file, as_attachment=True)
@application.route('/project-1')
def project1():
    return render_template('project-1.html')
@application.route('/contact',methods=['GET','POST'])
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
    application.run(debug=True,use_reloader=True)
