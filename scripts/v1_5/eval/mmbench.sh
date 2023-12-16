#!/bin/bash

SPLIT="mmbench_dev"

python -m llava.eval.model_vqa_mmbench \
    --model-path models/stablellava-13b/ \
    --model-base models/vicuna-13b-v1.5/ \
    --question-file ./playground/data/eval/mmbench/mmbench_dev.tsv \
    --answers-file ./playground/data/eval/mmbench/answers/$SPLIT/stablellava-13b.jsonl \
    --single-pred-prompt \
    --temperature 0 \
    --conv-mode vicuna_v1

mkdir -p playground/data/eval/mmbench/answers_upload/$SPLIT

python scripts/convert_mmbench_for_submission.py \
    --annotation-file ./playground/data/eval/mmbench/mmbench_dev.tsv \
    --result-dir ./playground/data/eval/mmbench/answers/$SPLIT \
    --upload-dir ./playground/data/eval/mmbench/answers_upload/$SPLIT \
    --experiment stablellava-13b
