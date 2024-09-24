from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    original_text = ''
    filtered_text = ''

    if request.method == 'POST':
        original_text = request.form.get('text')
        selected_filter = request.form.get('filter')

        if selected_filter == 'uppercase':
            filtered_text = original_text.upper()
        elif selected_filter == 'capitalize':
            filtered_text = original_text.capitalize()
        elif selected_filter == 'reverse':
            filtered_text = original_text[::-1]
        else:
            filtered_text = original_text

    return render_template('index.html', original_text=original_text, filtered_text=filtered_text)

if __name__ == '__main__':
    app.run(debug=True)

