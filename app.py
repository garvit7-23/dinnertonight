from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Load Hugging Face's text generation model
generator = pipeline("text-generation", model="gpt2")  # Replace with a model of your choice

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
        # Generate bio using Hugging Face model
        bio = generator(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
        print("Generated Bio:", bio)  # Debug log
        return jsonify({"bio": bio})
    except Exception as e:
        print("Error:", str(e))  # Debug log
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
