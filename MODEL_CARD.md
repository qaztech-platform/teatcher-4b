---
license: apache-2.0
language:
- en
- ru
pipeline_tag: text-generation
tags:
- education
- tutor
- edge
- nvidia-jetson
- deeptutor
- teatcher
- qwen3
library_name: transformers
---

# teatcher-4B (v0.1 preview — in training)

**The on-device tutor of the [TEA+T+CHER](https://teatcher.com) personal AI learning workstation.**
A compact 4B-class model fine-tuned for patient, step-by-step tutoring: building courses from
documents, drilling quizzes with citations to the exact source page, correcting misconceptions,
and answering study questions — entirely on-device, with no usage fees and no network required.

> 🚧 **Weights are in training and will be published here.** This card already follows the final
> format; TBD values below are filled in at release.

## Quick start

Ollama:

```bash
ollama run qaztech-platform/teatcher-4b
```

Transformers:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
m = "qaztech-platform/teatcher-4B"
tok = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, torch_dtype="auto", device_map="auto")
msgs = [{"role": "system", "content": "You are a patient tutor. Teach step by step, cite the source page."},
        {"role": "user", "content": "Quiz me on entropy from my thermodynamics notes."}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, enable_thinking=False, return_tensors="pt").to(model.device)
print(tok.decode(model.generate(ids, max_new_tokens=400)[0][ids.shape[1]:], skip_special_tokens=True))
```

Use `enable_thinking=False`: the model is trained without reasoning traces.

## Training (completed at release)

- Base: Qwen3-4B class, Apache-2.0 (final base and version stated here at release, with attribution).
- Method: LoRA (rank/alpha TBD, all linear layers), merged into the base weights, bf16.
- Data: synthetic tutoring dialogues (counts TBD), generated from public educational material
  and reviewed for this project. **No customer or workstation user data — ever.**
- Modes: course building from documents · step-by-step explanation · certification-style quiz
  generation with page citations · misconception correction.
- Languages: English, Russian.
- Filters: question and answer in the same language, no references to unseen source text,
  no mixed scripts, deduplication.
- Held-out eval: loss TBD, token accuracy TBD.

## Edge deployment

Sized for NVIDIA Jetson Orin Nano Super 8 GB: GGUF Q4_K_M (~2.5–3 GB) leaves room for the
system, DeepTutor and the user's document index. Recommended `num_ctx 8192`, power mode MAXN SUPER.

## Limitations

- Facts can be wrong. Inside the workstation the model runs with retrieval over the user's own
  documents (DeepTutor), and answers cite the source page — use it the same way standalone (RAG).
- A 4B model is a tutor, not an oracle: no professional medical, legal or financial advice.
- Capabilities outside the tutoring modes above are untested and not promised.

## Links

- Product: https://teatcher.com · Contact: access@teatcher.com
- Tutor environment (open source): https://github.com/HKUDS/DeepTutor

TEA+T+CHER is a registered trademark of AISC Technologies Ltd (United Kingdom), UK00004283802,
used under licence by AL SAFI FZE. NVIDIA and Jetson are trademarks of NVIDIA Corporation.
