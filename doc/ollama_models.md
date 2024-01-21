# ollama models

## Code

* codellama - people learning to code, including Python, C++, Java, PHP, Typescript (Javascript), C#, Bash and more.
* magicoder - high quality code
* mistral - approaches codellama 7B perf on code
* wizardcoder - based on code llama, focused on python

## Descriptions

model | size | description
--- | --- | ---
codellama:latest | 3.8 GB | Code Llama is a model for generating and discussing code, built on top of Llama 2. It’s designed to make workflows faster and efficient for developers and make it easier for people to learn how to code. It can generate both code and natural language about code. Code Llama supports many of the most popular programming languages used today, including Python, C++, Java, PHP, Typescript (Javascript), C#, Bash and more.
dolphin-mistral:latest | 4.1 GB | The Dolphin model by Eric Hartford, based on Mistral. This model is uncensored, available for both commercial and non-commercial use, and excels at coding. Updated to version 2.6.
dolphin-phi:latest | 1.6 GB | Dolphin Phi 2.6 is an uncensored model based on the 2.7B Phi model by Microsoft Research, using similar datasets as other versions of this model such as Dolphin Mixtral. It was created by Eric Hartford and Cognitive Computations.
llama-pro:latest | 4.6 BG | An expansion of Llama 2 that specializes in integrating both general language understanding and domain-specific knowledge, particularly in programming and mathematics. Awrite version of the original LLaMa model enhanced by the addition of transformer blocks by Tencent Applied Research Center (ARC).
llama2:latest | 3.8 GB  | Llama 2 is released by Meta Platforms, Inc. This model is trained on 2 trillion tokens, and by default supports a context length of 4096. Llama 2 Chat models are fine-tuned on over 1 million human annotations, and are made for chat.
magicoder:latest | 3.8 GB | Magicoder is a model family empowered by OSS-Instruct, a novel approach to enlightening LLMs with open-source code snippets for generating low-bias and high-quality instruction data for code. OSS-Instruct mitigates the inherent bias of the LLM-synthesized instruction data by empowering them with a wealth of open-source references to produce more diverse, realistic, and controllable data.
mistral:latest | 4.1 GB | The 7B model released by Mistral AI, updated to version 0.2. Mistral is a 7.3B parameter model, distributed with the Apache license. It is available in both instruct (instruction following) and text completion. The Mistral AI team has noted that Mistral 7B: Outperforms Llama 2 13B on all benchmarks. Outperforms Llama 1 34B on many benchmarks. Approaches CodeLlama 7B performance on code, while remaining good at English tasks.
phi:latest | 1.6 GB | Phi-2 is a small language model capable of common-sense reasoning and language understanding. It showcases “state-of-the-art performance” among language models with less than 13 billion parameters. A 2.7B language model by Microsoft Research.
solar:latest | 6.1 GB | Solar is the first open-source 10.7 billion parameter language model. It’s compact, yet remarkably powerful, and demonstrates state-of-the-art performance in models with parameters under 30B. This model leverages the Llama 2 architecture and employs the Depth Up-Scaling technique, integrating Mistral 7B weights into upscaled layers. On the H6 benchmark, this model outperforms models with up to 30B parameters, even the Mixtral 8X7B model.
wizardcoder | 3.8 GB | Wizard Coder is a code generation model based on Code Llama and focused on Python.
wizardlm-uncensored:latest | 7.4 GB | WizardLM Uncensored is a 13B parameter model based on Llama 2 uncensored by Eric Hartford. The models were trained against LLaMA-7B with a subset of the dataset, responses that contained alignment / moralizing were removed.
