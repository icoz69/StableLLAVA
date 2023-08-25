import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Process data and create LLaVA training format JSON.")
    parser.add_argument('--image_path', type=str, default='train_set/animal/', help='Path to the image directory.')
    parser.add_argument('--prompt_path', type=str, default='dataset/animal.json', help='Path to the JSON file containing prompts.')
    parser.add_argument('--save_path', type=str, default='train_ano/animal.json', help='Path to save the generated JSON file.')

    args = parser.parse_args()

    with open(args.prompt_path, 'r') as f:
        data = json.load(f)

    out_list = []

    for info in data:
        per_info = {}
        per_info['id'] = info['id'].zfill(12)
        per_info['image'] = os.path.join(args.image_path, info['id'].zfill(12) + '.jpg')
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

    with open(args.save_path, 'w') as file:
        json.dump(out_list, file)

if __name__ == "__main__":
    main()
