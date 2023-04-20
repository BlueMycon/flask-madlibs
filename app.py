from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story, stories

story_names = {story.story_name: story for story in stories}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def get_home():
    """Returns select field to choose a story"""

    story_names = [story.story_name for story in stories]

    return render_template("select-story.html",stories=story_names)

@app.get("/questions")
def get_root():
    """returns the madlibs input form for this story"""

    story = story_names[request.args.get("story_name")]

    return render_template("questions.html",
                           story_name=story.story_name,
                           prompts=story.prompts)

@app.get("/results/<story_name>")
def get_results(story_name):
    """displays the resulting story given the user's inputs"""

    story = story_names[story_name]
    result_text = story.get_result_text(request.args)
    
    return render_template("results.html", story=result_text)

