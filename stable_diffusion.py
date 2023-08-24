from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")
prompt_path = 'dataset/animal.json'
save_path = 'train_set/animal/'
# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()
with open(prompt_path,'r') as f:
   data = json.load(f)

for info in data:
    img = info['image'].split('/')[1]
    prompt = info['prompt']
    images = pipe(prompt=prompt).images[0]
    images.save(save_path+img)

