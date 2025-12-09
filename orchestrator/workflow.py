"""
Orchestrator - Coordinates the multi-agent workflow
"""
import json
from typing import Dict
from models.product import Product
from agents import (
    DataParserAgent,
    QuestionGenerationAgent,
    FAQGenerationAgent,
    ContentAssemblyAgent
)


class WorkflowOrchestrator:
    """
    Orchestrator that coordinates multiple agents in a pipeline workflow
    
    Workflow:
    1. DataParserAgent: Parse input data
    2. QuestionGenerationAgent: Generate questions
    3. FAQGenerationAgent: Generate answers
    4. ContentAssemblyAgent: Assemble pages
    """
    
    def __init__(self):
        self.name = "WorkflowOrchestrator"
        
        # Initialize agents
        self.data_parser = DataParserAgent()
        self.question_generator = QuestionGenerationAgent()
        self.faq_generator = FAQGenerationAgent()
        self.content_assembler = ContentAssemblyAgent()
        
        self.workflow_state = {}
    
    def execute_pipeline(self, input_file: str, product_b_data: Dict = None) -> Dict[str, any]:
        """
        Execute the complete workflow pipeline
        
        Args:
            input_file: Path to input JSON file
            product_b_data: Optional data for Product B (for comparison)
            
        Returns:
            Dictionary containing all generated outputs
        """
        results = {
            "workflow": "Multi-Agent Content Generation Pipeline",
            "agents_executed": [],
            "outputs": {}
        }
        
        # Step 1: Parse product data
        print(f"[{self.name}] Step 1: Parsing product data...")
        product_a = self.data_parser.parse_from_file(input_file)
        results["agents_executed"].append(self.data_parser.name)
        self.workflow_state["product_a"] = product_a
        
        # Step 2: Generate questions
        print(f"[{self.name}] Step 2: Generating questions...")
        questions = self.question_generator.generate_questions(product_a)
        results["agents_executed"].append(self.question_generator.name)
        self.workflow_state["questions"] = questions
        print(f"[{self.name}] Generated {len(questions)} questions")
        
        # Step 3: Generate FAQ answers
        print(f"[{self.name}] Step 3: Generating FAQ answers...")
        answers = self.faq_generator.generate_answers(product_a, questions)
        results["agents_executed"].append(self.faq_generator.name)
        self.workflow_state["answers"] = answers
        
        # Step 4: Assemble FAQ page
        print(f"[{self.name}] Step 4: Assembling FAQ page...")
        faq_page = self.content_assembler.assemble_faq_page(product_a, questions, answers)
        results["outputs"]["faq"] = faq_page
        
        # Step 5: Assemble Product page
        print(f"[{self.name}] Step 5: Assembling Product page...")
        product_page = self.content_assembler.assemble_product_page(product_a)
        results["outputs"]["product"] = product_page
        
        # Step 6: Assemble Comparison page (if Product B data provided)
        if product_b_data:
            print(f"[{self.name}] Step 6: Assembling Comparison page...")
            product_b = Product.from_dict(product_b_data)
            self.workflow_state["product_b"] = product_b
            comparison_page = self.content_assembler.assemble_comparison_page(product_a, product_b)
            results["outputs"]["comparison"] = comparison_page
        
        results["agents_executed"].append(self.content_assembler.name)
        
        print(f"[{self.name}] Pipeline execution complete!")
        return results
    
    def save_outputs(self, results: Dict, output_dir: str = "outputs"):
        """
        Save generated pages to JSON files
        
        Args:
            results: Results from execute_pipeline
            output_dir: Directory to save outputs
        """
        import os
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        outputs = results.get("outputs", {})
        
        # Save FAQ page
        if "faq" in outputs:
            faq_path = os.path.join(output_dir, "faq.json")
            with open(faq_path, 'w', encoding='utf-8') as f:
                json.dump(outputs["faq"], f, indent=2, ensure_ascii=False)
            print(f"[{self.name}] Saved: {faq_path}")
        
        # Save Product page
        if "product" in outputs:
            product_path = os.path.join(output_dir, "product_page.json")
            with open(product_path, 'w', encoding='utf-8') as f:
                json.dump(outputs["product"], f, indent=2, ensure_ascii=False)
            print(f"[{self.name}] Saved: {product_path}")
        
        # Save Comparison page
        if "comparison" in outputs:
            comparison_path = os.path.join(output_dir, "comparison_page.json")
            with open(comparison_path, 'w', encoding='utf-8') as f:
                json.dump(outputs["comparison"], f, indent=2, ensure_ascii=False)
            print(f"[{self.name}] Saved: {comparison_path}")
    
    def get_workflow_state(self) -> Dict:
        """Get current workflow state"""
        return {
            "orchestrator": self.name,
            "state": {
                "product_a_loaded": "product_a" in self.workflow_state,
                "product_b_loaded": "product_b" in self.workflow_state,
                "questions_generated": len(self.workflow_state.get("questions", [])),
                "answers_generated": len(self.workflow_state.get("answers", []))
            }
        }
