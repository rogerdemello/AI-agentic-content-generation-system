# Project Documentation

## Problem Statement

The challenge is to design and implement a modular agentic automation system that transforms structured product data into multiple content page formats (FAQ, Product Description, Comparison) with machine-readable JSON outputs. The system must demonstrate production-grade architecture with clear agent boundaries, orchestration patterns, and reusable content logic.

## Solution Overview

This system implements a **pipeline-based multi-agent architecture** where specialized agents work in sequence, each with a single, well-defined responsibility. The orchestrator coordinates the workflow, ensuring clean data flow and proper agent execution order.

### Key Components:
1. **Agents**: Specialized workers with single responsibilities
2. **Content Blocks**: Reusable transformation functions
3. **Template Engine**: Structured page generation system
4. **Orchestrator**: Pipeline coordination and state management
5. **Data Models**: Internal product representation

## Scopes & Assumptions

### In Scope:
- Multi-agent workflow implementation
- Automated question generation (15+ categorized questions)
- FAQ, Product, and Comparison page generation
- Machine-readable JSON output
- Modular, extensible architecture
- Template-based content generation
- Reusable content logic blocks

### Out of Scope:
- External data fetching or API integration
- UI/Frontend implementation
- LLM/GPT integration for content generation
- Database storage
- Authentication/Authorization

### Assumptions:
- Product data follows the defined schema
- All input data is provided in JSON format
- No external research or fact-checking required
- Product B (for comparison) can be fictional but must be structured
- System operates on provided data only

## System Design

### Architecture Pattern: Pipeline-Based Multi-Agent System

```
┌─────────────────────────────────────────────────────────────┐
│                   Workflow Orchestrator                      │
│                  (Pipeline Coordinator)                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Step 1: Data Parser Agent            │
        │  Input: JSON file                     │
        │  Output: Product model                │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Step 2: Question Generation Agent    │
        │  Input: Product model                 │
        │  Output: 15+ categorized questions    │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Step 3: FAQ Generation Agent         │
        │  Input: Product + Questions           │
        │  Output: Answers list                 │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Step 4: Content Assembly Agent       │
        │  Uses: Template Engine + Content      │
        │        Blocks                         │
        │  Output: 3 JSON pages                 │
        └───────────────────────────────────────┘
                            │
                            ▼
            ┌───────────────────────────┐
            │  FAQ Page (faq.json)      │
            │  Product Page             │
            │  Comparison Page          │
            └───────────────────────────┘
```

### Agent Responsibilities

#### 1. DataParserAgent
- **Responsibility**: Parse and validate raw product JSON
- **Input**: JSON file path or dictionary
- **Output**: Validated Product model
- **No global state**: Stateless parsing

#### 2. QuestionGenerationAgent
- **Responsibility**: Generate categorized user questions
- **Input**: Product model
- **Output**: List of question dictionaries (category, question)
- **Categories**: Informational, Safety, Usage, Purchase, Comparison, Technical

#### 3. FAQGenerationAgent
- **Responsibility**: Generate answers based on product data
- **Input**: Product model + Questions
- **Output**: List of answers
- **Logic**: Rule-based answer generation from product attributes

#### 4. ContentAssemblyAgent
- **Responsibility**: Assemble pages using templates and blocks
- **Input**: Product model(s)
- **Output**: Structured page data
- **Uses**: TemplateEngine, Content Blocks

### Content Logic Blocks

Reusable transformation functions in `blocks/content_blocks.py`:

1. **generate_benefits_block**: Transforms benefits into formatted content
2. **extract_usage_block**: Extracts and formats usage instructions
3. **extract_safety_block**: Formats safety and side effect information
4. **generate_ingredients_block**: Formats key ingredients/components
5. **generate_price_block**: Formats pricing information
6. **compare_ingredients_block**: Compares components between products
7. **compare_benefits_block**: Compares benefits between products
8. **compare_price_block**: Compares pricing between products
9. **generate_overview_block**: Creates product overview content

### Template Engine

Three specialized templates:

1. **FAQTemplate**: Structures FAQ with categories, questions, and answers
2. **ProductPageTemplate**: Multi-section product page with overview, benefits, ingredients, usage, safety, pricing
3. **ComparisonPageTemplate**: Side-by-side product comparison

Each template:
- Defines structured fields
- Accepts content blocks as input
- Returns machine-readable JSON
- Includes metadata for traceability

### Data Flow

```
Input JSON → Product Model → Questions → Answers → Templates → JSON Output
     │             │             │           │          │           │
     └─ Parser ────┘             │           │          │           │
                   └─ QGen ──────┘           │          │           │
                                 └─ FAQ Gen ─┘          │           │
                                              └─ Assembly┘           │
                                                         └─ Save ────┘
```

### Orchestration Strategy

**Pipeline Pattern** with sequential stages:
- Each agent executes only after previous completes
- State maintained in orchestrator
- Clear dependency chain
- Error propagation through pipeline
- Workflow state tracking

### Extensibility

The system is designed for easy extension:

- **New agents**: Add to pipeline without modifying existing agents
- **New content blocks**: Add to `blocks/` directory
- **New templates**: Implement Template interface
- **New question categories**: Extend QuestionGenerationAgent
- **New page types**: Add template and assembly method

### Technology Stack

- **Language**: Python 3.8+
- **Architecture**: Multi-agent pipeline
- **Data**: JSON for input/output
- **Models**: Dataclasses for type safety
- **No external APIs**: Pure logic-based generation

## Output Structure

All outputs follow this pattern:

```json
{
  "page_type": "string",
  "product_name": "string",
  "content": { ... },
  "metadata": {
    "generated_from": "template_name",
    "additional_info": "..."
  }
}
```

## Testing & Validation

Run the system:
```bash
python main.py
```

Outputs will be generated in `outputs/`:
- `faq.json`
- `product_page.json`
- `comparison_page.json`

All outputs are valid JSON and can be programmatically validated.

## Design Decisions

1. **Pipeline over DAG**: Sequential dependency chain is clear and sufficient
2. **Stateless agents**: Each agent is independent, no hidden state
3. **Dataclasses for models**: Type safety and clear contracts
4. **Rule-based generation**: No LLM needed, deterministic output
5. **Template pattern**: Separation of structure from content logic
6. **Content blocks**: DRY principle, reusable across pages
7. **JSON output**: Machine-readable, easy to validate and consume

## Conclusion

This system demonstrates production-grade agentic architecture with:
- Clear separation of concerns
- Modular, testable components
- Extensible design
- Type-safe data flow
- Deterministic, reproducible outputs
