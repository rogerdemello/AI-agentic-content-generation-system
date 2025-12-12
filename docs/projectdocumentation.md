# Project Documentation

## Overview

Pipeline-based system that takes product JSON and outputs FAQ, product page, and comparison JSONs. Four agents run sequentially, each handling one part of the process.

## Architecture

### Agents

Four agents run in order:

1. **DataParserAgent** (`agents/data_parser_agent.py`)
   - Parses raw JSON input into Product model
   - Validates required fields
   - Returns structured Product object

2. **QuestionGenerationAgent** (`agents/question_generation_agent.py`)
   - Generates 15+ questions across six categories
   - Categories: Informational, Safety, Usage, Purchase, Comparison, Technical
   - Returns list of (category, question) tuples

3. **FAQGenerationAgent** (`agents/faq_generation_agent.py`)
   - Generates answers using product attributes
   - Rule-based answer composition
   - Returns list of answer strings

4. **ContentAssemblyAgent** (`agents/content_assembly_agent.py`)
   - Assembles pages using templates and content blocks
   - Generates FAQ, Product, and Comparison pages
   - Returns structured JSON for each page type

### Content Blocks

Reusable transformation functions in `blocks/content_blocks.py`:

- `generate_overview_block()` — Product overview with key specs
- `generate_benefits_block()` — Formatted benefits list
- `generate_ingredients_block()` — Key ingredients display
- `extract_usage_block()` — Usage instructions
- `extract_safety_block()` — Safety and side effects
- `generate_price_block()` — Pricing information
- `compare_ingredients_block()` — Ingredient comparison
- `compare_benefits_block()` — Benefits comparison
- `compare_price_block()` — Price comparison

### Templates

Three page templates in `templates/template_engine.py`:

1. **FAQTemplate** — Structures FAQ page with categories, questions, and answers
2. **ProductPageTemplate** — Multi-section product page (overview, benefits, ingredients, usage, safety, pricing)
3. **ComparisonPageTemplate** — Side-by-side product comparison

Templates accept content blocks and return structured JSON with metadata.

### Data Flow

```
Input JSON → DataParserAgent → Product Model
                                      ↓
                          QuestionGenerationAgent → Questions
                                      ↓
                          FAQGenerationAgent → Answers
                                      ↓
                          ContentAssemblyAgent → 3 JSON Pages
                                      ↓
                          (FAQ, Product, Comparison)
```

## Orchestration

`WorkflowOrchestrator` in `orchestrator/workflow.py` runs the pipeline:

- `execute_pipeline(file_path)` - loads JSON from file
- `execute_pipeline_from_data(data)` - accepts dict directly

Manages state between agents and returns a summary.

## Web Interface

### Frontend (`public/index.html`)
- Single-page vanilla JavaScript UI
- Paste product JSON directly
- Generate and download results
- Mobile responsive

### API (`api/generate.py`)
- Serverless function for Vercel
- POST `/api/generate` with product_a (and optional product_b)
- Returns JSON with FAQ, Product, and Comparison pages
- Supports CORS and OPTIONS requests

## Deployment

### Vercel
- Configuration in `vercel.json`
- Python 3.x runtime
- Routes: `/api/*` to serverless, `/*` to static files
- Zero environment variables needed

### Local Development
- `python main.py` — Run pipeline from file
- `python run_local.py` — Start local server (port 8000)
- `python test_system.py` — Run test suite

## Testing

Test coverage in `test_system.py`:
- Product model validation
- Agent execution
- Question generation (15+ questions)
- FAQ structure
- Output JSON schema validation

## Design choices

- Pure Python stdlib (no deps)
- Agents are stateless
- Linear pipeline is enough
- Dataclass for Product model
- Rule-based (no LLMs)
- JSON outputs

## Extending

To add features:

- New agents: add to `WorkflowOrchestrator`
- New blocks: add functions to `blocks/content_blocks.py`
- New templates: add to `templates/template_engine.py`
- New question types: extend `QuestionGenerationAgent`
- New pages: add assembly method in `ContentAssemblyAgent`

## File Structure

```
├── agents/
│   ├── data_parser_agent.py
│   ├── question_generation_agent.py
│   ├── faq_generation_agent.py
│   └── content_assembly_agent.py
├── blocks/
│   └── content_blocks.py
├── templates/
│   └── template_engine.py
├── models/
│   └── product.py
├── orchestrator/
│   └── workflow.py
├── api/
│   └── generate.py
├── public/
│   └── index.html
├── main.py
├── test_system.py
└── vercel.json
```

## Output Format

All pages follow this structure:

```json
{
  "page_type": "faq|product|comparison",
  "product_name": "...",
  "content": {
    // Page-specific content
  },
  "metadata": {
    "generated_from": "template_name",
    "additional_info": "..."
  }
}
```
