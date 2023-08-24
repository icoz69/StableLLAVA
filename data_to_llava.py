import json
import os
image_path = 'train_set/animal/'
prompt_path = 'dataset/animal.json'
with open(prompt_path,'r') as f:
    data = json.load(f)
out_list = []

for info in data:
   per_info = {}
   per_info['id'] = info['id'].zfill(12)
   per_info['image'] = image_path + info['id'].zfill(12)+'.jpg'
   conv = []
   per_human = {}
   per_gpt = {}
   per_human['from'] = 'human'
   per_human['value'] = info['question']
   per_gpt['from'] = 'gpt'
   per_gpt['value'] = info['answer']
   conv.append(per_human)
   conv.append(per_gpt)
   per_info['conversations'] = conv
   out_list.append(per_info)

with open('train_ano/animal.json','w') as file:
   json.dump(out_list,file)

