"""
Main entry point for the Multi-Agent Content Generation System
"""
from orchestrator import WorkflowOrchestrator


def main():
    """Execute the complete content generation pipeline"""
    
    print("=" * 60)
    print("Kasparro AI Agentic Content Generation System")
    print("=" * 60)
    
    # Initialize orchestrator
    orchestrator = WorkflowOrchestrator()
    
    # Define Product B (fictional competitor product)
    product_b_data = {
        "product_name": "RadiantGlow Vitamin C Essence",
        "concentration": "15% Vitamin C",
        "suitable_for": "All skin types",
        "key_ingredients": ["Vitamin C", "Ferulic Acid", "Vitamin E"],
        "benefits": ["Brightening", "Anti-aging", "Antioxidant protection"],
        "how_to_use": "Apply 3-4 drops in the evening after cleansing",
        "side_effects": "May cause redness for very sensitive skin",
        "price": "₹899"
    }
    
    # Execute pipeline
    results = orchestrator.execute_pipeline(
        input_file="input_data.json",
        product_b_data=product_b_data
    )
    
    # Save outputs
    orchestrator.save_outputs(results)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Pipeline Summary")
    print("=" * 60)
    print(f"Agents Executed: {', '.join(results['agents_executed'])}")
    print(f"Pages Generated: {', '.join(results['outputs'].keys())}")
    
    # Print workflow state
    state = orchestrator.get_workflow_state()
    print(f"\nWorkflow State:")
    print(f"  - Product A loaded: {state['state']['product_a_loaded']}")
    print(f"  - Product B loaded: {state['state']['product_b_loaded']}")
    print(f"  - Questions generated: {state['state']['questions_generated']}")
    print(f"  - Answers generated: {state['state']['answers_generated']}")
    
    print("\n" + "=" * 60)
    print("All outputs saved to outputs/ directory")
    print("=" * 60)


if __name__ == "__main__":
    main()
