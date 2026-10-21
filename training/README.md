# Training and publication plan

This document states, ahead of release, what teatcher-4B is trained for and what will be published.

## Objective

A patient on-device tutor: step-by-step explanations, Socratic guiding questions, quiz
generation with page-accurate citations to user documents, bilingual (English / Russian).

## Base model

An Apache-2.0-licensed 4B-class base (candidate under evaluation). The final choice, its
version and full attribution will be stated in `MODEL_CARD.md` and `NOTICE` at release.

## Data policy

- No customer or workstation user data is used — ever. The workstation sends us nothing.
- Training mixes public educational corpora, permissively licensed instruction data and
  synthetic tutoring dialogues generated and reviewed for this project.
- A summary of the data mixture will be published with the weights.

## What will be published

1. Fine-tuned weights (safetensors) and GGUF quantizations (Q4_K_M, Q8_0) — Hugging Face
2. Model card with evaluation notes and limitations — honest ones, no benchmark theater
3. Ollama package: `ollama pull <namespace>/teatcher-4b`
4. Reproducible packaging notes for Jetson Orin Nano 8 GB (`docs/jetson.md`)
