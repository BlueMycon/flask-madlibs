from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

current_story = excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def get_root():
    """returns the madlibs input form for this story"""

    return render_template("questions.html", prompts=current_story.prompts)

@app.get("/results")
def get_results():
    """displays the resulting story given the user's inputs"""

    story = current_story.get_result_text(request.args)
    return render_template("results.html", story=story)

