from google import genai
import os

# 🔐 Put your API key here
API_KEY = "AIzaSyC-QB7lBQeLMpV5fZOlQLGDE3YxpHph3_8"

# Create client
client = genai.Client(api_key=API_KEY)

print("\n🎯 CareerBot - AI Career Guidance Assistant")
print("Choose a mode:")
print("1. Career Path Guidance")
print("2. Skill Roadmap")
print("3. Resume Improvement")
print("4. Project Suggestions")
print("5. Interview Preparation")
print("Type 'exit' to quit\n")

modes = {
    "1": "You are a career counselor guiding students on choosing the right career path.",
    "2": "You are a skill mentor creating structured learning roadmaps.",
    "3": "You are a resume expert improving resumes for freshers.",
    "4": "You are a project mentor suggesting practical project ideas.",
    "5": "You are an interview coach preparing candidates for interviews."
}

while True:
    mode = input("Select Mode (1-5): ")

    if mode.lower() == "exit":
        print("CareerBot: Stay focused and keep growing 🚀")
        break

    if mode not in modes:
        print("Invalid choice. Select between 1 to 5.")
        continue

    print("\nAsk your question (type 'back' to change mode):")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "back":
            break
        if user_input.lower() == "exit":
            print("CareerBot: All the best for your future! 🌟")
            exit()

        prompt = f"""
{modes[mode]}
Answer clearly, practically, and in structured points.

User Question:
{user_input}
"""

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            print("\nCareerBot:\n", response.text)
            print("-" * 60)

        except Exception as e:
            print("\n❌ Error:", e)
            print("Possible reasons:")
            print("• API key is invalid")
            print("• Free quota exhausted")
            print("• Internet issue")
            print("• Model temporarily unavailable\n")

