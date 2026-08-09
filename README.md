# NotifyAI

NotifyAI is an AI-powered notification and message
prioritization agent.

The goal is to analyze incoming messages, determine their importance
and urgency, and eventually decide how the user should be notified.

## Current Features

- FastAPI backend
- Local LLM using Ollama
- AI-based message analysis
- Structured JSON output
- Pydantic validation
- Priority Engine
- Rule-based priority overrides
- Promotional message filtering

## Current Architecture

Message
↓
AI Analyzer
↓
Structured Analysis
↓
Priority Engine
↓
Final Priority

## Tech Stack

- Python 3.12
- FastAPI
- Ollama
- Llama 3.2
- Pydantic
