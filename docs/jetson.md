# Running teatcher-4B on NVIDIA Jetson Orin Nano (8 GB)

The model is sized for 8 GB of shared memory: a 4B-class model in Q4_K_M quantization
occupies roughly 2.5–3 GB, leaving room for the system, DeepTutor and your documents.

## Install (after release)

```bash
# Ollama on Jetson (arm64)
curl -fsSL https://ollama.com/install.sh | sh

# pull the model
ollama pull qaztech-platform/teatcher-4b

# talk to it
ollama run qaztech-platform/teatcher-4b
```

## Recommended settings

| Setting | Value | Why |
| --- | --- | --- |
| Quantization | Q4_K_M | best quality/size balance for 8 GB |
| Context (`num_ctx`) | 8192 | course chapters fit; raise cautiously — context eats memory |
| Power mode | MAXN SUPER | full 67 TOPS; switch in the Ubuntu top bar |

## Air-gapped install

For closed contours, Ollama and the GGUF file can be transferred on removable media and
installed without internet access. A step-by-step offline procedure will be published here
together with the release.
