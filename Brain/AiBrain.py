import os
# get the absolute path of the project root directory
root_dir = os.path.dirname(os.path.abspath(__file__)) # jarvisOpenAI\Brain

# specify the relative file paths for the chat log and API secrets files
chat_logs_file = os.path.join(root_dir, "..", "DataBase","chat_log.txt")
api_secrets_file = os.path.join(root_dir, "..", "Data", "API_SECRETS.txt") # ".." goes one directory up"

fileOpen = open(api_secrets_file, "r")
API = fileOpen.read()
fileOpen.close()
# print(API)

import openai
from dotenv import load_dotenv
# Load the API key and set up the OpenAI API client
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def replyBrain(question, chat_log_file=chat_logs_file):
    # Load the chat log from the specified file
    try:
        with open(chat_log_file, "r") as file:
            chat_log_template = file.read()
    except FileNotFoundError:
        raise Exception("Chat log file not found")

    prompt = f"{chat_log_template} INSTRUCTION_U : {question}\nJARVIS : "
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nINSTRUCTION_U : {question}\nJARVIS :{answer}"

    # Write the updated chat log back to the file
    with open(chat_log_file, "w") as file:
        file.write(chat_log_template_update)

    return answer


# while True:
#     kk = input("ENTER QUERY : ")
#     print(replyBrain(kk))
# reply = replyBrain("What's the time ?")
# print(reply)
  