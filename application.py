from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def show_user_application():
	"""display the application form to the user."""

	return render_template("application-form.html")

@app.route("/application-response")
def respond_to_users_application():
	"respond to the user to let them know their application has been received."

	first_name = request.args.get("firstname")
	last_name = request.args.get("lastname")
	radio_position = request.args.get("radio-job")
	chosen_salary = request.args.get("salary-choice")
	relevant_skills = request.args.get("skills")

	return render_template("application-response.html",
							first=first_name,
							last=last_name,
							position=radio_position,
							salary=chosen_salary,
							skills=relevant_skills)

if __name__ == "__main__":
    app.run(debug=True)
