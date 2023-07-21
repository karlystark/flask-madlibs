from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def choose_story():
    return render_template(
        "story-select.html",
        stories = stories.values()
    )


@app.get('/prompts')
def show_form():
    """function collects prompts from story instance and passes them as a
    template to create input form"""
    story_code = request.args["story_code"]
    story = stories[story_code]
    prompts = story.prompts

    return render_template (
        "questions.html",
        story_code = story_code,
        title = story.title,
        prompts=prompts
    )


@app.get('/<story_code>/results')
def get_results_and_display(story_code):
    """function gets form inputs and renders story result"""
    story = stories[story_code]
    answers = request.args
    result_story = story.get_result_text(answers)


    return render_template(
        "results.html",
        title = story.title,
        result_story=result_story
    )
