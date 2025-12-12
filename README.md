# Agentic Content Generator

A modular, agent-based system that generates structured content (FAQ, product pages, and comparisons) from product JSON data.

## Overview
A lightweight multi-agent pipeline that parses product data, generates questions, composes answers, and assembles exportable JSON pages using reusable content blocks and templates.

## Features
- 🤖 **Multi-agent architecture** with clear responsibilities
- 🔄 **Pipeline orchestration** coordinating specialized agents
- 🧩 **Reusable content blocks** for transformations
- 📄 **Template-based generation** (FAQ, Product, Comparison)
- 📊 **Machine-readable JSON outputs**
- 🌐 **Web interface** for easy interaction
- 🚀 **Vercel-ready** serverless deployment
- 🐍 **Pure Python** (no external dependencies)

## Live Demo

Visit the web interface to generate content:
1. Paste your product JSON data
2. Click "Generate Content"
3. Download the generated FAQ, Product, and Comparison pages

## Quick Start

### Option 1: Web Interface (Recommended)

Deploy to Vercel:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

Then open the deployed URL and use the web interface.

### Option 2: Command Line

```bash
# Run the pipeline locally
python main.py

# Run tests
python test_system.py
```

### Option 3: API Endpoint

```bash
# Start local development server
vercel dev

# Make API request
curl -X POST http://localhost:3000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"product_a": {...}}'
```

## Project Structure

```
├── api/                 # Vercel serverless functions
│   └── generate.py      # API endpoint for content generation
├── public/              # Frontend web interface
│   └── index.html       # Web UI
├── agents/              # Agent implementations
│   ├── data_parser_agent.py
│   ├── question_generation_agent.py
│   ├── faq_generation_agent.py
│   └── content_assembly_agent.py
├── blocks/              # Reusable content logic
├── templates/           # Page templates
├── models/              # Data models
├── orchestrator/        # Workflow orchestration
├── outputs/             # Generated JSON files
└── docs/                # Documentation
```

## API Reference

### POST /api/generate

Generate content from product data.

**Request Body:**
```json
{
  "product_a": {
    "product_name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "suitable_for": "Oily, Combination",
    "key_ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "how_to_use": "Apply 2–3 drops in the morning",
    "side_effects": "Mild tingling for sensitive skin",
    "price": "₹699"
  },
  "product_b": { /* optional for comparison */ }
}
```

**Response:**
```json
{
  "success": true,
  "outputs": {
    "faq": { /* FAQ page JSON */ },
    "product": { /* Product page JSON */ },
    "comparison": { /* Comparison page JSON (if product_b provided) */ }
  },
  "agents_executed": ["DataParserAgent", "QuestionGenerationAgent", ...]
}
```

## Deployment

### Vercel (Recommended)

1. Push your code to GitHub
2. Import the repository in Vercel
3. Deploy (no configuration needed)

Or use the CLI:
```bash
vercel --prod
```

### Manual Deployment

The project includes:
- `vercel.json` - Vercel configuration
- `api/generate.py` - Serverless function
- `public/index.html` - Static frontend
- `requirements.txt` - Python dependencies (none required)

## Development

### Run locally
```bash
# Backend only
python main.py

# With Vercel dev server (includes frontend + API)
vercel dev
```

### Run tests
```bash
python test_system.py
```

### Code quality
```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

## Architecture

Multi-agent pipeline with specialized roles:

1. **DataParserAgent** - Parses and validates product JSON
2. **QuestionGenerationAgent** - Generates 15+ categorized questions
3. **FAQGenerationAgent** - Generates answers from product data
4. **ContentAssemblyAgent** - Assembles pages using templates

See [docs/projectdocumentation.md](docs/projectdocumentation.md) for detailed architecture.

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — see [LICENSE](LICENSE)
