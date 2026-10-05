from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flashcard Generator</title>
</head>

<body>

    <h1>AI Flashcard Generator</h1>

    <form method="POST">

        <h3>Enter your study notes:</h3>

        <textarea name="notes"
                  rows="15"
                  cols="80"
                  placeholder="Enter your notes here..."
                  required></textarea>

        <br><br>

        <button type="submit">Generate Flashcards</button>

    </form>

    {% if flashcards %}

        <h2>Generated Flashcards</h2>

        <pre>{{ flashcards }}</pre>

    {% endif %}

</body>
</html>
"""


def generate_flashcards(notes):

    sentences = [
        sentence.strip()
        for sentence in notes.replace("\n", " ").split(".")
        if sentence.strip()
    ]

    flashcards = ""

    count = min(5, len(sentences))

    for i in range(count):

        sentence = sentences[i]

        flashcards += f"""
Flashcard {i + 1}

Question:
What is the important point about:
{sentence}?

Answer:
{sentence}.

------------------------------
"""

    return flashcards


@app.route("/", methods=["GET", "POST"])
def home():

    flashcards = ""

    if request.method == "POST":

        notes = request.form["notes"]

        flashcards = generate_flashcards(notes)

    return render_template_string(
        HTML_PAGE,
        flashcards=flashcards
    )


if __name__ == "__main__":
    app.run(debug=True)