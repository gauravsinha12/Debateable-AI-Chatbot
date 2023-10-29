---
license: mit
base_model: TheBloke/zephyr-7B-alpha-GPTQ
tags:
- generated_from_trainer
model-index:
- name: zephyr-support-chatbot
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# zephyr-support-chatbot

This model is a fine-tuned version of [TheBloke/zephyr-7B-alpha-GPTQ](https://huggingface.co/TheBloke/zephyr-7B-alpha-GPTQ) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- training_steps: 250

### Training results



### Framework versions

- Transformers 4.34.1
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
