# Applied AI Engineer Challenge: Multi-Agent Content Generation System

## 🎯 Objective
Design and implement a modular agentic automation system that takes a small product dataset and automatically generates structured, machine-readable content pages. The focus is on engineering and design ability, not domain expertise.

### Key Evaluation Areas
- Multi-agent workflows
- Automation graphs
- Reusable content logic
- Template-based generation
- Structured JSON output
- System abstraction & documentation

## 📦 Product Data (Input Example)
- Product Name: AeroClean Air Purifier
Concentration: 99.7% HEPA Filtration Efficiency
- Skin Type: Suitable for all room sizes
- Key Ingredients: HEPA Filter, Activated Carbon Layer, Ionizer
- Benefits: Removes dust, allergens, smoke; Improves air quality
- How to Use: Plug in and run on auto-mode; replace filter every 6 months
- Side Effects: Ionizer mode may produce slight ozone smell
- Price: ₹5,499

*No external facts or research allowed. System must operate on this data type.*

## 🧪 Assignment Requirements
1. **Parse & understand product data**: Convert to internal model.
2. **Generate at least 15 categorized user questions**: Categories like Informational, Safety, Usage, Purchase, Comparison, etc.
3. **Define & implement templates**: FAQ Page, Product Description Page, Comparison Page.
4. **Create reusable content logic blocks**: Functions/modules to transform data into copy.
5. **Assemble 3 pages using your system**:
   - FAQ Page (5+ Q&As)
   - Product Page
   - Comparison Page (GlowBoost vs fictional Product B)
6. **Output each page as clean, machine-readable JSON** (e.g., `faq.json`, `product_page.json`, `comparison_page.json`).
7. **Pipeline must run via agents**: Not a single-script GPT wrapper.

## 🚫 What This Assignment Is NOT
- Not a prompting assignment
- Not a single big function calling GPT
- Not a content writing test
- Not a UI/website challenge

## 🏗 System Requirements
- **Clear Agent Boundaries**: Single responsibility, defined input/output, no hidden global state.
- **Automation Flow/Orchestration Graph**: DAG, pipeline, state machine, message-passing, orchestrator/worker.
- **Reusable Logic Blocks**: E.g., generate-benefits-block, extract-usage-block, compare-ingredients-block.
- **Template Engine**: Structured fields, rules, formatting, dependencies on blocks.
- **Machine-Readable Output**: All pages as JSON.

## 📁 Repository Requirements
- GitHub repo: `ai-agentic-content-generation-system-<first_name-last_name>`
- Must include `docs/projectdocumentation.md` with:
  - Problem Statement
  - Solution Overview
  - Scopes & Assumptions
  - System Design (mandatory)
  - (Optional) Diagrams, flowcharts, sequence diagrams

## 📥 Submission
- Share the GitHub repo link.

## 🧮 Evaluation Criteria
1. **Agentic System Design (45%)**: Responsibilities, modularity, extensibility, flow correctness.
2. **Types & Quality of Agents (25%)**: Roles, boundaries, input/output correctness.
3. **Content System Engineering (20%)**: Template and logic block quality, composability.
4. **Data & Output Structure (10%)**: JSON correctness, clean mapping from data to output.

## 🧠 Purpose
Measures ability to design production-style agentic systems.

---

# What You Can Expect — The Engineering Environment & Learning Curve

- **Steep learning curve, high expectations, unmatched growth.**
- **Real engineering from day one**: Not shallow intern work.

### 1. Work on sophisticated AI systems
- Exposure to advanced AI system structuring, multi-step reasoning, and building adaptive, reliable components.

### 2. Learn real architecture and system design
- Involvement in system integration, interfaces, contracts, robustness, and maintainability.
- Shift from "coder" to "engineer" mindset.

### 3. Professional engineering standards
- Write production-quality code, participate in reviews, own system parts, and be expected to reason, not just execute.

### 4. Fast growth with strong engineers
- Learn to articulate reasoning, review deeply, think beyond just running code.
- Develop pattern recognition, trade-off analysis, and decision-making skills.

### 5. Master the craft of building with AI
- Use AI as an engineering multiplier for design, implementation, testing, and iteration.

**This is a place for driven people to grow extremely fast.**
- Fast pace, high standards, complex systems.
- Interns are expected to rise to the challenge and become high-level engineers.
