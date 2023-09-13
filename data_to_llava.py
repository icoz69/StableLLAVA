import json
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process data and create LLaVA training format JSON.")
    parser.add_argument('--image_path', type=str, default='train_set/', help='Path to the image directory.')
    parser.add_argument('--dataset_path', type=str, default='dataset/', help='Path to the directory containing JSON datasets.')
    parser.add_argument('--save_path', type=str, default='train_ano/', help='Path to save the generated JSON files.')

    args = parser.parse_args()

    json_files = [filename for filename in os.listdir(args.dataset_path) if filename.endswith('.json')]

    for json_file in json_files:
        json_file_path = os.path.join(args.dataset_path, json_file)

        with open(json_file_path, 'r') as f:
            data = json.load(f)

        out_list = []

        for info in data:
            per_info = {}
            per_info['id'] = info['id'].zfill(12)
            per_info['image'] = os.path.join(args.image_path, info.replace('.json'.''), per_info['id'] + '.jpg')
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

        output_file_path = os.path.join(args.save_path, json_file)

        with open(output_file_path, 'w') as file:
            json.dump(out_list, file)


if __name__ == "__main__":
    main()
