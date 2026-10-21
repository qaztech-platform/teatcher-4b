#!/usr/bin/env python3
"""Minimal local chat with teatcher-4B through the Ollama API.

Works once the model is installed:  ollama pull qaztech-platform/teatcher-4b
No external dependencies — standard library only.
"""
import json
import sys
import urllib.request

MODEL = "qaztech-platform/teatcher-4b"
API = "http://localhost:11434/api/chat"


def ask(messages):
    req = urllib.request.Request(
        API,
        data=json.dumps({"model": MODEL, "messages": messages, "stream": False}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)["message"]["content"]


def main():
    print("teatcher-4B · local tutor (Ctrl+C to quit)")
    history = []
    try:
        while True:
            user = input("\nyou > ").strip()
            if not user:
                continue
            history.append({"role": "user", "content": user})
            try:
                answer = ask(history)
            except OSError:
                sys.exit("Ollama is not reachable on localhost:11434 — is it running, "
                         "and is the model pulled?")
            history.append({"role": "assistant", "content": answer})
            print(f"\ntutor > {answer}")
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
