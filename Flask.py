from flask import Flask, render_template, request,url_for, redirect
import os
import model

app = Flask(__name__)
fname=""
l=None
result=""
@app.route('/')
def index():
	global l
	l = model.load_model()

	return render_template('index.html', fname= fname, result=result)

@app.route('/i')
def inference():
	global result
	image = model.get_image(fname)
	result,ic,p = l.predict(image)
	return redirect(url_for("index"))

@app.route('/lol')
def lol1():
	return lol.lol()

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
	global fname
	if request.method=='POST':
		f = request.files["imgfile"]
		f.save("static\\"+f.filename)
		fname = "static\\"+f.filename

		return redirect(url_for('inference'))
		# return fname


app.run(debug=True)