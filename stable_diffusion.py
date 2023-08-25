import argparse
import json
from diffusers import DiffusionPipeline
import torch

def main():
    parser = argparse.ArgumentParser(description="Diffuser Pipeline for processing images with prompts.")
    parser.add_argument('--prompt_path', type=str, default='dataset/animal.json', help='Path to the JSON file containing prompts.')
    parser.add_argument('--save_path', type=str, default='train_set/animal/', help='Path to save processed images.')

    args = parser.parse_args()

    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")

    with open(args.prompt_path, 'r') as f:
        data = json.load(f)

    for info in data:
        img = info['image'].split('/')[1]
        prompt = info['prompt']
        images = pipe(prompt=prompt).images[0]
        images.save(args.save_path + img)

if __name__ == "__main__":
    main()
