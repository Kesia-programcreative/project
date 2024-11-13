import google.generativeai as genai
genai.configure(api_key="AIzaSyCoYzJU2VHpaOgBq0CoElAuy_MyRJIhVhw")
model = genai.GenerativeModel("gemini-1.5-flash")
system_prompt = "answer as a tutor who helps in clearing questions with creative ideas and real life experience ,is funny, answers everything in 2 or 3 lines ,always explains in a way that a 5 year old child can understand it never says no or gives errors"
def tutor (user_input):
    prompt = system_prompt + user_input
    response = model.generate_content(prompt)
    return response.text
if(__name__== "__main__"):
    print("HI,HOW CAN I HELP YOU")
    while True:
        user_input = input("student: ")
        if user_input.lower() == "exit":
            print("HAVE A GREAT DAY!")
            break
        response = tutor(user_input)
        print(f"tutor: {response}")