### Fine-Tuning Gemma Models with LoRA using the Databricks Dolly 15k Dataset

**Links : [Dataset](https://huggingface.co/datasets/databricks/databricks-dolly-15k) , [Gemma](https://www.kaggle.com/models/google/gemma)**

#### Project Description:
This project aims to enhance the performance of Gemma Causal Language Models by fine-tuning them with Low Rank Adaptation (LoRA) techniques, using the Databricks Dolly 15k dataset. 

The process involves configuring the Keras backend for JAX, preprocessing the dataset to filter and format examples, and initializing the [GemmaCausalLM model](https://keras.io/api/keras_nlp/models/gemma/gemma_causal_lm/). The model's initial responses to sample prompts are recorded to establish a baseline.

Subsequently, LoRA is enabled on the model to reduce the number of trainable parameters, and the model is fine-tuned using the prepared dataset. The effectiveness of the fine-tuning process is evaluated by comparing the model's responses to the same prompts before and after the fine-tuning.

The project demonstrates the potential of using LoRA for efficient fine-tuning of large language models. It also provides insights into various hyperparameters and settings that can be adjusted to optimize model performance, such as increasing the dataset size, adjusting the number of training epochs, and tuning learning rates.
