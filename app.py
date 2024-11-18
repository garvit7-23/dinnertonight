from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)



from flask_cors import CORS
CORS(app)  # Enable CORS for all routes





# Set your OpenAI API key 
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API Key is missing.")


@app.route("/", methods=["GET", "HEAD"])
def home():
    if request.method == "HEAD":
        return "", 200
    try:
        return render_template("index.html")
    except Exception as e:
        return jsonify({"error": f"Error rendering index page: {str(e)}"}), 500


@app.route("/generate-bio", methods=["POST"])
def generate_bio():
    data = request.json
    print("Received data:", data)  # Debug log

    user_input = f"""
    Career: {data.get('career')}
    Personality: {data.get('personality')}
    Interests: {data.get('interests')}
    Relationship Goals: {data.get('goals')}
    """
    print("Formatted user input:", user_input)  # Debug log

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if needed
            messages=[
                {"role": "system", "content": "You are an assistant who generates bios based on user details."},
                {"role": "user", "content": f"Generate a personalized bio based on these details:\n{user_input}"}
            ]
        )
        bio = response['choices'][0]['message']['content'].strip()
        print("Generated Bio:", bio)  # Debug log
        return jsonify({"bio": bio})
    except Exception as e:
        print("Error:", str(e))  # Debug log
        return jsonify({"error": str(e)}), 500


if _name_ == "_main_":
    app.run(debug=True)
