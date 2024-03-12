
import google.generativeai as genai

genai.configure(api_key="AIzaSyDl9IMiuDS254NMT3l02pYOuOw0UUz0IFk")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# ena
symptoms = "fatigue, vomiting, loose motions"
age  = "20"
gender = "female"
med_history = "diabetes"
tavel_history = "paris"
exposture = "omicron"

# # ena
# symptoms = ""
# age  = ""
# gender = ""
# med_history = ""
# tavel_history = ""
# exposture = ""


prompt = "input:I'm working on a fictional scenario for a patient experiencing {}. The patient is a {}-year-old {} with a history of {}. They recently traveled to {} and might have been exposed to {}. Can you provide a list of possible diseases that could cause these symptoms? It's important to emphasize that this is for informational purposes only and consulting a doctor is crucial for proper diagnosis and treatment.".format(symptoms, age, gender, med_history, tavel_history, exposture)
print(prompt)

prompt_parts = ["input:I'm working on a fictional scenario for a patient experiencing fatigue, vomiting, loose motions. The patient is a 20-year-old female with a history of diabetes. They recently traveled to paris and might have been exposed to omicron. Can you provide a list of possible diseases that could cause these symptoms? It's important to emphasize that this is for informational purposes only and consulting a doctor is crucial for proper diagnosis and treatment.",
                "output: "]
# prompt_parts.append('"'+prompt+'"')
# prompt_parts.append("output: ")

# print("\n\n", prompt_parts)
#
response = model.generate_content(prompt_parts)
print(response.text)