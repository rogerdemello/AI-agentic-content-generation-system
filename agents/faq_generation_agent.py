"""
FAQ Generation Agent - Generates FAQ content from questions
"""
from typing import List, Dict
from models.product import Product
import blocks.content_blocks as blocks


class FAQGenerationAgent:
    """Agent responsible for generating FAQ answers"""
    
    def __init__(self):
        self.name = "FAQGenerationAgent"
    
    def generate_answers(self, product: Product, questions: List[Dict]) -> List[str]:
        """
        Generate answers for questions based on product data
        
        Args:
            product: Product model
            questions: List of question dictionaries with 'category' and 'question'
            
        Returns:
            List of answer strings
        """
        answers = []
        
        for q in questions:
            category = q.get("category", "")
            question = q.get("question", "")
            
            # Generate answer based on category and question content
            answer = self._generate_answer(product, category, question)
            answers.append(answer)
        
        return answers
    
    def _generate_answer(self, product: Product, category: str, question: str) -> str:
        """Generate specific answer based on category and question"""
        
        question_lower = question.lower()
        
        # What is the product
        if "what is" in question_lower and product.product_name.lower() in question_lower:
            return f"{product.product_name} is a product with {product.concentration}, {product.suitable_for}. It contains {', '.join(product.key_ingredients)}."
        
        # Key features
        if "key features" in question_lower or "features" in question_lower:
            return f"Key features include {product.concentration}, {', '.join(product.key_ingredients)}, and benefits such as {', '.join(product.benefits)}."
        
        # What makes it effective
        if "effective" in question_lower or "makes" in question_lower:
            return f"The effectiveness comes from its {product.concentration} and key components like {', '.join(product.key_ingredients)}."
        
        # Side effects
        if "side effect" in question_lower:
            return product.side_effects if product.side_effects else "No known side effects when used as directed."
        
        # Safety for daily use
        if "safe" in question_lower and "daily" in question_lower:
            safety = "Yes, it is safe for daily use. " 
            if product.side_effects:
                safety += f"However, note: {product.side_effects}"
            return safety
        
        # Precautions
        if "precaution" in question_lower:
            if product.side_effects:
                return f"Be aware: {product.side_effects}. Follow the usage instructions carefully."
            return "Follow the usage instructions: " + product.how_to_use
        
        # How to use
        if "how" in question_lower and "use" in question_lower:
            return product.how_to_use
        
        # When to use
        if "when" in question_lower:
            return f"Use according to instructions: {product.how_to_use}"
        
        # How often
        if "how often" in question_lower:
            return f"Follow the recommended usage: {product.how_to_use}"
        
        # Best way to get results
        if "best way" in question_lower or "results" in question_lower:
            return f"For optimal results, {product.how_to_use}. Consistent use is recommended."
        
        # Price/cost
        if "cost" in question_lower or "price" in question_lower or "much" in question_lower:
            return f"{product.product_name} is priced at {product.price}."
        
        # Where to buy
        if "where" in question_lower and "buy" in question_lower:
            return f"You can purchase {product.product_name} at the listed price of {product.price}."
        
        # Worth the price
        if "worth" in question_lower:
            return f"Yes, {product.product_name} offers {', '.join(product.benefits)} at {product.price}, providing excellent value."
        
        # Comparison
        if "compare" in question_lower or "different" in question_lower:
            return f"{product.product_name} stands out with its {product.concentration} and unique combination of {', '.join(product.key_ingredients)}."
        
        # Technical spec
        if category == "Technical":
            return f"The {product.concentration} refers to the key specification of {product.product_name}."
        
        # Default answer
        return f"For {product.product_name}: {product.concentration}, {product.suitable_for}. Benefits include {', '.join(product.benefits)}."
    
    def get_output(self) -> Dict:
        """Return agent metadata"""
        return {
            "agent": self.name,
            "responsibility": "Generate answers for FAQ questions based on product data"
        }
