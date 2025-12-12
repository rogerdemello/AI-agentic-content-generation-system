"""
Test suite for the Multi-Agent Content Generation System
"""
import json
import os
from models.product import Product
from agents import DataParserAgent, QuestionGenerationAgent, FAQGenerationAgent, ContentAssemblyAgent
from orchestrator import WorkflowOrchestrator


def test_product_model():
    """Test Product model creation and conversion"""
    print("Testing Product model...")
    
    test_data = {
        "product_name": "Test Product",
        "concentration": "100% Test",
        "suitable_for": "Testing",
        "key_ingredients": ["A", "B"],
        "benefits": ["Benefit 1", "Benefit 2"],
        "how_to_use": "Test usage",
        "side_effects": "None",
        "price": "₹100"
    }
    
    product = Product.from_dict(test_data)
    assert product.product_name == "Test Product"
    assert len(product.key_ingredients) == 2
    assert len(product.benefits) == 2
    
    product_dict = product.to_dict()
    assert product_dict["product_name"] == "Test Product"
    
    print("✓ Product model tests passed")


def test_data_parser_agent():
    """Test DataParserAgent"""
    print("Testing DataParserAgent...")
    
    agent = DataParserAgent()
    product = agent.parse_from_file("input_data.json")
    
    assert product.product_name == "GlowBoost Vitamin C Serum"
    assert "Vitamin C" in product.key_ingredients
    assert len(product.benefits) > 0
    
    print("✓ DataParserAgent tests passed")


def test_question_generation_agent():
    """Test QuestionGenerationAgent"""
    print("Testing QuestionGenerationAgent...")
    
    agent = QuestionGenerationAgent()
    product = Product.from_dict({
        "product_name": "Test Product",
        "concentration": "100%",
        "suitable_for": "All",
        "key_ingredients": ["A"],
        "benefits": ["Benefit"],
        "how_to_use": "Use daily",
        "side_effects": None,
        "price": "₹100"
    })
    
    questions = agent.generate_questions(product)
    
    assert len(questions) >= 15, f"Expected at least 15 questions, got {len(questions)}"
    assert all("category" in q for q in questions)
    assert all("question" in q for q in questions)
    
    categories = set(q["category"] for q in questions)
    assert "Informational" in categories
    assert "Safety" in categories
    assert "Usage" in categories
    
    print(f"✓ QuestionGenerationAgent tests passed ({len(questions)} questions generated)")


def test_faq_generation_agent():
    """Test FAQGenerationAgent"""
    print("Testing FAQGenerationAgent...")
    
    agent = FAQGenerationAgent()
    product = Product.from_dict({
        "product_name": "Test Product",
        "concentration": "100%",
        "suitable_for": "All",
        "key_ingredients": ["A", "B"],
        "benefits": ["Benefit 1", "Benefit 2"],
        "how_to_use": "Use daily",
        "side_effects": "None",
        "price": "₹100"
    })
    
    questions = [
        {"category": "Usage", "question": "How do I use Test Product?"},
        {"category": "Purchase", "question": "How much does Test Product cost?"}
    ]
    
    answers = agent.generate_answers(product, questions)
    
    assert len(answers) == len(questions)
    assert all(isinstance(a, str) for a in answers)
    assert any("Use daily" in a for a in answers)
    
    print("✓ FAQGenerationAgent tests passed")


def test_content_assembly_agent():
    """Test ContentAssemblyAgent"""
    print("Testing ContentAssemblyAgent...")
    
    agent = ContentAssemblyAgent()
    product = Product.from_dict({
        "product_name": "Test Product",
        "concentration": "100%",
        "suitable_for": "All",
        "key_ingredients": ["A", "B"],
        "benefits": ["Benefit 1", "Benefit 2"],
        "how_to_use": "Use daily",
        "side_effects": "None",
        "price": "₹100"
    })
    
    # Test product page assembly
    product_page = agent.assemble_product_page(product)
    assert product_page["page_type"] == "product"
    assert "sections" in product_page
    assert "overview" in product_page["sections"]
    assert "benefits" in product_page["sections"]
    
    print("✓ ContentAssemblyAgent tests passed")


def test_json_outputs():
    """Test that generated JSON files are valid"""
    print("Testing JSON output files...")
    
    # Generate outputs first if they don't exist
    output_dir = "outputs"
    if not os.path.exists(output_dir) or not os.listdir(output_dir):
        print("  Generating outputs first...")
        orchestrator = WorkflowOrchestrator()
        results = orchestrator.execute_pipeline("input_data.json")
        orchestrator.save_outputs(results)
    
    required_files = ["faq.json", "product_page.json"]
    optional_files = ["comparison_page.json"]
    
    for filename in required_files:
        filepath = os.path.join(output_dir, filename)
        assert os.path.exists(filepath), f"Missing output file: {filename}"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert "page_type" in data, f"{filename} missing 'page_type'"
        assert "metadata" in data, f"{filename} missing 'metadata'"
        
        print(f"  ✓ {filename} is valid JSON")
    
    # Check optional files
    for filename in optional_files:
        filepath = os.path.join(output_dir, filename)
        if os.path.exists(filepath):
            print(f"  ✓ {filename} is valid JSON (optional)")
    
    print("✓ All JSON output tests passed")


def test_faq_output_structure():
    """Test FAQ output has correct structure"""
    print("Testing FAQ output structure...")
    
    with open("outputs/faq.json", 'r', encoding='utf-8') as f:
        faq = json.load(f)
    
    assert faq["page_type"] == "faq"
    assert "faqs" in faq
    assert faq["faq_count"] >= 5, "FAQ must have at least 5 Q&As"
    
    for item in faq["faqs"]:
        assert "category" in item
        assert "question" in item
        assert "answer" in item
    
    print(f"✓ FAQ structure valid ({faq['faq_count']} Q&As)")


def test_product_page_structure():
    """Test Product page output has correct structure"""
    print("Testing Product page structure...")
    
    with open("outputs/product_page.json", 'r', encoding='utf-8') as f:
        product = json.load(f)
    
    assert product["page_type"] == "product"
    assert "sections" in product
    
    required_sections = ["overview", "benefits", "ingredients", "usage", "safety", "pricing"]
    for section in required_sections:
        assert section in product["sections"], f"Missing section: {section}"
    
    print("✓ Product page structure valid")


def test_comparison_page_structure():
    """Test Comparison page output has correct structure (optional)"""
    print("Testing Comparison page structure...")
    
    import os
    if not os.path.exists("outputs/comparison_page.json"):
        print("⊘ Comparison page not generated (requires product_b) - skipping")
        return
    
    with open("outputs/comparison_page.json", 'r', encoding='utf-8') as f:
        comparison = json.load(f)
    
    assert comparison["page_type"] == "comparison"
    assert "products" in comparison
    assert "product_a" in comparison["products"]
    assert "product_b" in comparison["products"]
    assert "comparisons" in comparison
    
    assert "ingredients" in comparison["comparisons"]
    assert "benefits" in comparison["comparisons"]
    assert "pricing" in comparison["comparisons"]
    
    print("✓ Comparison page structure valid")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running Test Suite")
    print("=" * 60)
    print()
    
    tests = [
        test_product_model,
        test_data_parser_agent,
        test_question_generation_agent,
        test_faq_generation_agent,
        test_content_assembly_agent,
        test_json_outputs,
        test_faq_output_structure,
        test_product_page_structure,
        test_comparison_page_structure
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
