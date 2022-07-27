from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Malak"
password = "Mm90"
facebook_friends=["Joleen","Layan","Noa", "Lolo"]


@app.route('/', methods=['GET', 'POST']) 
def login():
	if request.method == 'POST':
		us= request.form['username']
		ps = request.form['password']
		if us==username and ps==password :
			return redirect(url_for('home'))
		else:
			return render_template ('login.html')
	else:
			return render_template ('login.html')  

@app.route('/home') 
def home():
	return render_template("home.html",facebook_friends=facebook_friends)



@app.route('/friend_exists/<string:friend>') 
def friend_exists(friend):
	is_friend = friend in facebook_friends
	return render_template('friend_exists.html',is_friend = is_friend)





if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)