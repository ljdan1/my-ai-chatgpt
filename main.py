import groq
import os

client = groq.Groq(api_key="")  


print("📘 Hey there! I’m your Study Buddy ")
name = input("What’s your name? ")
print(f"Hi {name}, let’s tackle your study questions together! ")


while True:
    user_input = input(f"{name}: ")
    
    if user_input.lower() == "exit":
        print("Good luck on your studies! You’ve got this! ")
        break
    elif user_input.strip() == "":
        print("✏️ Please enter a question or topic so I can help you better!")
        continue
    else:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly study buddy who helps students revise for exams with encouraging tips and simple explanations."
                },
                {"role": "user", "content": user_input}
            ]
        )


        reply = response.choices[0].message.content
        print("📚 StudyBuddy:", reply)

    
