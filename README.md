# AI Agentic Content Generation System

Automated product content generator using a multi-agent pipeline. Takes JSON product data and outputs FAQ pages, product descriptions, and comparison tables.

Built with pure Python (no external dependencies).

## What it does

- Parses product JSON and generates FAQ/product/comparison pages
- Four agents handle parsing, question generation, answers, and assembly
- Web UI for quick testing (paste JSON, get results)
- REST API at `/api/generate`
- Deploys to Vercel with no config

## Usage

```bash
# Run the pipeline
python main.py

# Tests
python test_system.py

# Start dev server
python run_local.py
```

Or call it from code:

```python
from orchestrator.workflow import WorkflowOrchestrator

result = WorkflowOrchestrator().execute_pipeline_from_data({
    "product_name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "suitable_for": "Oily, Combination",
    "key_ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "how_to_use": "Apply 2-3 drops morning and evening",
    "side_effects": "Mild tingling possible",
    "price": "₹699"
})
```

Deploy:
```bash
vercel
```

## Project Structure

```
├── agents/              # Four agent implementations
├── blocks/              # Reusable content transformations
├── templates/           # Page templates (FAQ, Product, Comparison)
├── models/              # Product data model
├── orchestrator/        # Pipeline coordinator
├── api/                 # Serverless endpoint
├── public/              # Web interface
├── main.py              # CLI entry point
└── test_system.py       # Test suite
```

## How it works

1. DataParserAgent validates the input
2. QuestionGenerationAgent creates 15+ questions
3. FAQGenerationAgent generates answers
4. ContentAssemblyAgent builds the final pages

Outputs: `faq.json`, `product_page.json`, `comparison_page.json`

More details in `docs/projectdocumentation.md`.

## API Reference

**POST /api/generate**

Request body:
```json
{
  "product_a": {
    "product_name": "...",
    "concentration": "...",
    "suitable_for": "...",
    "key_ingredients": [...],
    "benefits": [...],
    "how_to_use": "...",
    "side_effects": "...",
    "price": "..."
  },
  "product_b": { ... }
}
```

Response:
```json
{
  "success": true,
  "outputs": {
    "faq": { ... },
    "product": { ... },
    "comparison": { ... }
  }
}
```

## Development

```bash
# Install pre-commit hooks (optional)
pip install pre-commit
pre-commit install

# Run code quality checks
pre-commit run --all-files
```

## License

MIT
