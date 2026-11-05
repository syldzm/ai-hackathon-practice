from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "")
        answer = f"입력한 질문: {question}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
