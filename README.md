# teatcher-4B

**The on-device tutor model of the [TEA+T+CHER](https://teatcher.com) personal AI learning workstation.**

teatcher-4B is a compact (4B-class) language model fine-tuned for patient, step-by-step tutoring:
building courses from documents, drilling quizzes with citations to the exact source page, and
answering study questions — entirely on-device, with no usage fees and no network required.
It ships on NVIDIA Jetson Orin Nano Super (8 GB) hardware inside the TEA+T+CHER workstation
and powers the open-source [DeepTutor](https://github.com/HKUDS/DeepTutor) learning environment.

## Status

> 🚧 **Training in progress. Weights and GGUF quantizations will be published here and on Hugging Face.**

- [x] Name and repositories reserved (GitHub · Hugging Face · Kaggle · ModelScope · Ollama)
- [ ] Base model selected and announced (Apache-2.0-licensed candidate)
- [ ] Fine-tuning on tutoring dialogues
- [ ] GGUF quantization for 8 GB edge devices
- [ ] Publication: weights, model card, evaluation notes
- [ ] `ollama push` — one-command install everywhere

## Why on-device

Learning works with the network cable unplugged: in homes, studios, schools, clinics and
government training contours where documents must never leave the building. No per-question
fees, no account, no cloud dependency. Cloud frontier models remain an optional addition on
the owner's own API key.

## Repository layout

| Path | What's inside |
| --- | --- |
| `MODEL_CARD.md` | Hugging Face model card (mirrored to the HF repo) |
| `Modelfile` | Ollama packaging recipe |
| `docs/jetson.md` | Running on NVIDIA Jetson Orin Nano 8 GB |
| `examples/chat.py` | Minimal local chat example (Ollama API) |
| `training/README.md` | Training and publication plan, data policy |

## Quick start (after release)

```bash
ollama run qaztech-platform/teatcher-4b
```

Until the weights land, see [teatcher.com](https://teatcher.com) for the workstation this model is built for.

## Mirrors

| Platform | Location |
| --- | --- |
| Hugging Face | [qaztech-platform/teatcher-4B](https://huggingface.co/qaztech-platform/teatcher-4B) |
| Ollama | [qaztech-platform/teatcher-4b](https://ollama.com/qaztech-platform/teatcher-4b) |
| ModelScope | qaztechplatform/teatcher-4B |
| Kaggle | QAZTECH / teatcher-4b |

## License and trademarks

Code and documentation in this repository are released under the Apache License 2.0 (see `LICENSE`).
The license of the model weights will be stated at release and will match the base model's terms,
with full attribution. See `NOTICE` for trademark information.
