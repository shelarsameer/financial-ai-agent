# Financial Agent

A powerful multi-agent system for financial analysis and research using Groq's AI models.

## Features

- **Finance AI Agent**: Provides stock data, analyst recommendations, fundamentals, and company news
- **Web Search Agent**: Searches the web for relevant financial information
- **Multi-Agent System**: Combines the capabilities of both agents for comprehensive analysis

## Installation

1. Clone this repository
2. Install dependencies:
```
pip install phi-client openai groq yfinance python-dotenv
```

3. Create a `.env` file in the project root with your API keys:
```
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key
```

## Usage

### Running the CLI Agent

```python
python financial_agent.py
```

This will analyze NVDA stock, providing analyst recommendations and latest news.

### Running the Web Playground

```python
python playground.py
```

This launches a web interface where you can interact with the financial agents.

## Project Structure

- `financial_agent.py`: Main CLI implementation with multi-agent setup
- `playground.py`: Web interface for interacting with the agents

## Models Used

- Groq's llama3-70b-8192 for high-quality financial analysis and insights

## Note

This project uses API keys for Groq. Make sure you have a valid API key from [Groq's console](https://console.groq.com/). 