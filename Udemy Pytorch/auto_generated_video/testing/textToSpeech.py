import requests
from moviepy.audio.io.AudioFileClip import AudioFileClip
import pandas as pd

key = "af233048324f53c647cc209a940dc9be"


# Generate a random integer between 0 and 9

def get_saved_audio(name):
    return AudioFileClip(f"temp/audio/ramayan-gk/{name}.mp3")




# def get_audio(text, name):
#     # random_number = random.randint(0, 10000)
#     chunk_size = 1024
#     url = "https://api.elevenlabs.io/v1/text-to-speech/u8mujqx12FGe4jOwcE3r"
#     '''Old Voice'''
#     # 7xcjjRC0S6h4mxrYMKuZ
#     headers = {
#         "Accept": "audio/mpeg",
#         "Content-Type": "application/json",
#         "xi-api-key": key
#     }
#     data = {
#         "text": text,
#         "model_id": "eleven_multilingual_v1",
#         "voice_settings": {
#             "stability": 0.56,
#             "similarity_boost": 0.4
#         }
#     }
#
#     response = requests.post(url, json=data, headers=headers)
#     with open(f'temp/audio/ramayan-gk/{name}.mp3', 'wb') as f:
#         for chunk in response.iter_content(chunk_size=chunk_size):
#             print('hh')
#             if chunk:
#                 f.write(chunk)
#     # return AudioFileClip(f"temp/audio/ramayan-gk/{name}.mp3")
#
#
# # get_audio('अगला प्रश्न ,', "next_question")
#
#
# df = pd.read_csv("gk_questions/ramayan-gk.csv")
#
# start = 1
# till = 40
#
# for index, row in df.iterrows():
#     if int(row['index']) < start:
#         continue
#     elif int(row['index']) > till:
#         break
#     print(row['index'])
#     allClipPerQuiz = []
#     questionText = str(row['question']).strip()
#     options = [" अ). " + str(row['o1']).strip()[3:], " ब). " + str(row['o2']).strip()[3:],
#                " स). " + str(row['o3']).strip()[3:], " द). " + str(row['o4']).strip()[3:]]
#     correctOption = ['a', 'b', 'c', 'd'].index(str(row['c_option']).strip())
#     opt = ["A", "B", "C", "D"]
#
#     '''-----------------------Audio--------------------------------------------------------'''
#     textToSpeak = questionText + "Option A " + options[0][2:] + ", Option B " + options[1][2:] + ", Option C " + options[2][2:] + ", Option D " + options[3][2:]
#     ansToSpeak = "सही जबाब.. Option " + opt[correctOption] + "," + options[correctOption][2:]
#     get_audio(textToSpeak, f"question{str(row['index'])}")
#     get_audio(ansToSpeak, f"ans{str(row['index'])}")
