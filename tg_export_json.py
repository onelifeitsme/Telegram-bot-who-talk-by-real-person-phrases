import json

messages_from_json = []
dialog = []

with open('result.json', 'r', encoding='utf-8') as temp:
    data = json.load(temp)
    ls = data['messages']
    for i in ls:
        if 'from' in i:
            messages_from_json.append(i)


count = 0
for i in range(len(messages_from_json)):
    if messages_from_json[count]['from'] == 'PUT HERE THE NAME OF PERSON 1 DROM DIALOGS' \
            and len(messages_from_json[count]['text']) > 0 \
            and messages_from_json[count+1]['from'] == 'PUT HERE THE NAME OF PERSON 2 DROM DIALOGS' \
            and len(messages_from_json[count+1]['text']) > 0 and type(messages_from_json[count+1]['text']) is str:
        dialog.append({
            f'u: {messages_from_json[count]["text"]}': f'{messages_from_json[count+1]["text"]}'
        })
    count += 1


with open('boltun.txt', 'w', encoding='utf-8') as temp:
    for i in dialog:
        for k in i.keys():
            temp.write(k)
            temp.write('\n')
        for v in i.values():
            temp.write(v)
            temp.write('\n')
