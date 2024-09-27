import os
import sys
import json
import re
def extract_subtitles(transcript):
    pattern = r'\d+\r\n\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\r\n(.*?)(?=\r\n\r\n|\Z)'
    matches = re.findall(pattern, transcript, re.DOTALL)
    return [match.strip() for match in matches]
def list_files(directory):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
        return []
dir=os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.basename(dir)
vtt_HAR_FILES= list_files(dir)
with open(dir+'\\iam.txt','w') as file:
    pass
for i in vtt_HAR_FILES:
    if i.endswith('.har'):
        with open(dir+'\\'+i , "r") as file:
            json_data=json.load(file)
        print(json_data)
        for s in json_data['log']['entries']:
            transcript=s['response']['content']['text']
            if not "thumb-sprites.jpg" in transcript:
                transcript_list=extract_subtitles(transcript)
                with open(dir+f'\\{parent_folder}.txt','a') as file:
                    for line in transcript_list:
                        file.writelines(line+'\n')


        
