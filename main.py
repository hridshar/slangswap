from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# 🔐 Load your OpenAI API key securely from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ""
    if request.method == 'POST':
        user_text = request.form.get('slang', '')

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert translator of informal and Gen Z slang English into clear, formal English. "
                            "Translate any slang or casual phrase to its most appropriate formal meaning, preserving original intent. "
                            "Here is a glossary of common slang terms and their meanings to guide you:\n\n"

                            "- rizz: charisma or ability to attract romantic interest\n"
                            "- drip: stylish or fashionable clothing\n"
                            "- no cap: being honest or truthful\n"
                            "- pulling: attracting romantic interest\n"
                            "- gyatt: a large or curvy buttocks (not a firearm; do not confuse with 'gat')\n"
                            "- gat: a slang term for firearm or gun\n"
                            "- swag or swagger: confidence, style, or charm\n"
                            "- flex: to show off or boast\n"
                            "- ghosting: suddenly cutting off all communication\n"
                            "- stan: an enthusiastic or obsessed fan\n"
                            "- tea: gossip or personal information\n"
                            "- sus: suspicious or untrustworthy\n"
                            "- lit: exciting, excellent, or fun\n"
                            "- woke: socially aware and politically conscious\n"
                            "- slaps: something very good, especially music\n"
                            "- cap: a lie or falsehood\n"
                            "- bread: money\n"
                            "- fire: excellent or amazing\n"
                            "- salty: bitter or upset\n"
                            "- basic: mainstream or unoriginal\n"
                            "- shook: shocked or surprised\n"
                            "- lowkey: secretly or quietly\n"
                            "- highkey: openly or obviously\n"
                            "- mood: something relatable or expressing feeling\n"
                            "- bet: agreement or confirmation\n"
                            "- fam: close friends or family\n"
                            "- shade: subtle disrespect or criticism\n"
                            "- vibe: the atmosphere or feeling\n"
                            "- chill: to relax\n"
                            "- deadass: seriously or honestly\n"
                            "- finna: going to or about to\n"
                            "- yeet: to throw or discard forcefully\n"
                            "- OG: original or authentic\n"
                            "- boujee: luxurious or high-class\n"
                            "- clap back: a sharp or witty response\n\n"

                            "When you encounter slang not on this list, use your training knowledge to translate it appropriately into clear, formal English."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Translate this sentence into formal English:\n\n'{user_text}'"
                    }
                ],
                temperature=0
            )

            if response.choices and response.choices[0].message and response.choices[0].message.content:
                translation = response.choices[0].message.content.strip()
            else:
                translation = "Sorry, I couldn't generate a translation."

        except Exception as e:
            translation = f"Error: {str(e)}"

    return render_template("index.html", translation=translation)


# 🟢 Run the Flask app (important for Replit or local run)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
