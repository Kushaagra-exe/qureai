data = {
    'name': 'dcdc',
    'email': '',
    'message': '',
    'age': 'dcsdc',
    'gender': 'dscdcsd',
    'symptoms': 'dscdcds',
    'med_history': 'dcsdc',
    'tavel_history': 'cdscdsc',
    'exposture': 'csdcds'
}
prompts = [
    "I'm working on a fictional scenario for a patient experiencing {}. The patient is a {}-year-old {} with",
    "a history of {}",
    "They recently traveled to {} ",
    "and might have been exposed to {}",
    "Can you provide a list of possible diseases that could cause these symptoms? It's important to emphasize that this is for informational purposes only and consulting a doctor is crucial for proper diagnosis and treatment.",
    "Please only provide the list of possible diseases and information in a list form about them nothing else "
]

symptoms = data['symptoms']
age = data['age']
gender = data['gender']
med_history = data['med_history']
tavel_history = data['tavel_history']
exposture = data['exposture']
final_prompt = prompts[0].format(symptoms, age, gender)
if (med_history):
    final_prompt = final_prompt + prompts[1].format(med_history)
else:
    final_prompt = final_prompt + "no medical history"

if (tavel_history):
    final_prompt = final_prompt + prompts[2].format(tavel_history)
else:
    final_prompt = final_prompt + "NO recent travelling"

if (exposture):
    final_prompt = final_prompt + prompts[3].format(exposture)

final_prompt = final_prompt + prompts[4] + prompts[5]

jsonresp = {
    "input": final_prompt,
    "output": ""
}

print(str(jsonresp))