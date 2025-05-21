# Vitteey Sahaayak

> A Next-Gen Financial Intelligence System Powered by Collaborative AI Agents

## Overview

Vitteey Sahaayak is a financial analysis system that leverages multiple AI agents working in concert to deliver comprehensive market insights. Built on the powerful Groq LLM (llama-3.3-70b-versatile), it combines real-time market data, web intelligence, and advanced analytics to provide actionable financial insights.

## Core Capabilities

### 1. Real-Time Market Intelligence
- Live stock price tracking and analysis
- Financial metrics computation
- Market trend identification
- Expert-level recommendations

### 2. Advanced Web Intelligence
- Multi-source data aggregation
- Cross-reference validation
- Pattern recognition
- Automated insight extraction

### 3. News Analysis
- Real-time financial news monitoring
- Sentiment analysis
- Impact assessment
- Trend detection

### 4. Deep Web Analysis
- Financial website crawling
- Content synthesis
- Market research automation
- Insight generation

## Technical Stack

- **AI Engine**: Groq (llama-3.3-70b-versatile)
- **Framework**: phidata
- **Data Sources**: yfinance, duckduckgo-search
- **Web Tools**: spider-client
- **News Source**: Hacker News

## Quick Start

```bash
# Clone and setup
git clone https://github.com/yourusername/Vitteey-Sahaayak.git
cd Vitteey-Sahaayak

# Environment setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure
echo "GROQ_API_KEY=your_api_key_here" > .env

# Launch
python main.py
```

## Architecture

```
Vitteey-Sahaayak/
├── Agent/
│   ├── agents.py      # Agent implementations
│   └── multiAgent.py  # Agent orchestration
├── main.py           # Entry point
└── requirements.txt  # Dependencies
```

## Key Features

- **Multi-Agent Collaboration**: Four specialized agents working in harmony
- **Real-Time Analysis**: Instant market insights and updates
- **Data-Driven Insights**: Comprehensive analysis from multiple sources
- **Source Verification**: All insights backed by verifiable sources
- **Structured Output**: Clear, tabulated data presentation

## Use Cases

- Investment research and analysis
- Market trend monitoring
- Financial news impact assessment
- Pattern recognition in market data
- Investment strategy development

## Contributing

We welcome contributions to enhance agent capabilities, add features, or improve documentation.

## License

Licensed under the terms of the included [LICENSE](LICENSE) file.

---

*Transform your financial analysis with the power of collaborative AI intelligence.*
