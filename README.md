# Kasparro AI Agentic Content Generation System

A modular multi-agent system for automated content generation from product data.

## Overview
This system demonstrates production-grade agentic architecture for transforming structured product data into multiple content page formats (FAQ, Product Description, Comparison) with machine-readable JSON outputs.

## Architecture
- **Modular Agents**: Each agent has single responsibility with clear input/output contracts
- **Orchestration**: Pipeline-based workflow coordinating multiple agents
- **Content Logic Blocks**: Reusable transformation functions
- **Template Engine**: Structured page generation system

## Project Structure
```
├── agents/              # Individual agent implementations
│   ├── data_parser_agent.py
│   ├── question_generation_agent.py
│   ├── faq_generation_agent.py
│   └── content_assembly_agent.py
├── blocks/              # Reusable content logic blocks
│   └── content_blocks.py
├── templates/           # Page templates
│   └── template_engine.py
├── models/              # Data models and schemas
│   └── product.py
├── orchestrator/        # Workflow orchestration
│   └── workflow.py
├── outputs/             # Generated JSON files
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
├── docs/                # Documentation
│   └── projectdocumentation.md
├── input_data.json      # Sample input data
├── main.py              # Entry point
├── test_system.py       # Test suite
└── requirements.txt     # Dependencies
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- No external dependencies (uses Python standard library only)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd kasparro-ai-agentic-content-generation-system

# No pip install needed - uses standard library only
```

### Running the System
```bash
# Run the complete pipeline
python main.py

# Run tests
python test_system.py
```

### Output
The system generates three JSON files in the `outputs/` directory:
- **faq.json**: FAQ page with 16 Q&As across 6 categories
- **product_page.json**: Complete product page with 6 sections
- **comparison_page.json**: Side-by-side product comparison

## System Components

### Agents
1. **DataParserAgent**: Parses and validates product JSON
2. **QuestionGenerationAgent**: Generates 15+ categorized questions
3. **FAQGenerationAgent**: Generates answers from product data
4. **ContentAssemblyAgent**: Assembles pages using templates

### Content Blocks
9 reusable transformation functions for generating structured content:
- Benefits, Usage, Safety, Ingredients, Pricing
- Overview, Comparisons (ingredients, benefits, pricing)

### Templates
- **FAQTemplate**: Structured FAQ with categories
- **ProductPageTemplate**: Multi-section product page
- **ComparisonPageTemplate**: Product comparison

## Testing
```bash
python test_system.py
```

Tests validate:
- Agent functionality and outputs
- JSON structure and validity
- Content completeness
- System integration

## Documentation
See `docs/projectdocumentation.md` for:
- Problem statement and solution overview
- Detailed system design and architecture
- Agent boundaries and responsibilities
- Data flow and orchestration patterns
- Design decisions and trade-offs

## Features
✅ Modular multi-agent architecture  
✅ Pipeline-based orchestration  
✅ 16 categorized questions generated  
✅ 3 page types (FAQ, Product, Comparison)  
✅ Machine-readable JSON output  
✅ Reusable content logic blocks  
✅ Template-based generation  
✅ Zero external dependencies  
✅ Comprehensive test suite  

## License
This is an assignment project for Kasparro AI Engineer Challenge.
