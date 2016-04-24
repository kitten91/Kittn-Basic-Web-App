from flask import Flask, request, render_template, session

app = Flask(__name__)


app.secret_key = "supersecret"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def show_user_application():
	"""display the application form to the user."""

	return render_template("application-form.html")

@app.route("/application")
def respond_to_users_application():

    session["firstname"] = request.args["firstname"]
    session["lastname"] = request.args["lastname"]
    session["salary"] = int(request.args["salary"])
    session["radio-job"] = request.args["radio-job"]
    session["skills"] = request.args["skills"]

    return render_template("application.html",
							first=session["firstname"],
							last=session["lastname"],
							salary=session["salary"],
							position=session["radio-job"],
							skills=session["skills"])


if __name__ == "__main__":
    app.run(debug=True)
