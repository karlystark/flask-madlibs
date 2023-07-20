from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def choose_story():


@app.get('/prompts')
def show_form():
    """function collects prompts from story instance and passes them as a
    template to create input form"""

    prompts = silly_story.prompts

    return render_template (
        "questions.html",
        prompts=prompts
    )


@app.get('/results')
def get_results_and_display():
    """function gets form inputs and renders story result"""

    answers = request.args
    result_story = silly_story.get_result_text(answers)


    return render_template(
        "results.html",
        result_story=result_story
    )
