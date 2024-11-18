from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from flask_cors import CORS
CORS(app)  # Enable CORS for all routes

# Inbuilt function to generate bio
def generate_bio_from_input(data):
    career = data.get('career', 'Unknown Career')
    personality = data.get('personality', 'Unknown Personality')
    interests = data.get('interests', 'Unknown Interests')
    goals = data.get('goals', 'Unknown Goals')
    
    # Simple formatted bio
    return f"Career: {career}\nPersonality: {personality}\nInterests: {interests}\nGoals: {goals}"

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

    try:
        # Use inbuilt function to generate bio
        bio = generate_bio_from_input(data)
        print("Generated Bio:", bio)  # Debug log
        return jsonify({"bio": bio})
    except Exception as e:
        print("Error:", str(e))  # Debug log
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
