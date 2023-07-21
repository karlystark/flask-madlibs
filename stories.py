"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.get_result_text(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def get_result_text(self, answers):
        """Return result text from dictionary of {prompt: answer, ...}."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story(
    "fantasy",
    "A Fantasy Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

story3 = Story(
    "animals",
    "An Animal Story",
    ["animal", "plural_noun", "verb", "adjective", "adverb", "noun"],
    """Walking home, we saw a {animal} fighting some {plural_noun} who {verb}
    near our house. What a {adjective} sight! They battled {adverb}, until they
    fell asleep cuddling in the {noun}."""
)

stories = {s.code: s for s in [story1, story2, story3]}