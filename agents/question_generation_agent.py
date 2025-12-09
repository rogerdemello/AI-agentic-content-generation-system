"""
Question Generation Agent - Generates categorized user questions
"""
from typing import List, Dict
from models.product import Product


class QuestionGenerationAgent:
    """Agent responsible for generating categorized user questions"""
    
    def __init__(self):
        self.name = "QuestionGenerationAgent"
        self.categories = [
            "Informational",
            "Safety", 
            "Usage",
            "Purchase",
            "Comparison",
            "Technical"
        ]
    
    def generate_questions(self, product: Product) -> List[Dict[str, str]]:
        """
        Generate categorized questions based on product data
        
        Args:
            product: Product model
            
        Returns:
            List of dictionaries with 'category' and 'question' keys
        """
        questions = []
        
        # Informational questions
        questions.extend([
            {
                "category": "Informational",
                "question": f"What is {product.product_name}?"
            },
            {
                "category": "Informational",
                "question": f"What are the key features of {product.product_name}?"
            },
            {
                "category": "Informational",
                "question": f"What makes {product.product_name} effective?"
            }
        ])
        
        # Safety questions
        questions.extend([
            {
                "category": "Safety",
                "question": f"Are there any side effects of using {product.product_name}?"
            },
            {
                "category": "Safety",
                "question": f"Is {product.product_name} safe for daily use?"
            },
            {
                "category": "Safety",
                "question": f"What precautions should I take when using {product.product_name}?"
            }
        ])
        
        # Usage questions
        questions.extend([
            {
                "category": "Usage",
                "question": f"How do I use {product.product_name}?"
            },
            {
                "category": "Usage",
                "question": f"When should I use {product.product_name}?"
            },
            {
                "category": "Usage",
                "question": f"How often should I use {product.product_name}?"
            },
            {
                "category": "Usage",
                "question": f"What is the best way to get results from {product.product_name}?"
            }
        ])
        
        # Purchase questions
        questions.extend([
            {
                "category": "Purchase",
                "question": f"How much does {product.product_name} cost?"
            },
            {
                "category": "Purchase",
                "question": f"Where can I buy {product.product_name}?"
            },
            {
                "category": "Purchase",
                "question": f"Is {product.product_name} worth the price?"
            }
        ])
        
        # Comparison questions
        questions.extend([
            {
                "category": "Comparison",
                "question": f"How does {product.product_name} compare to other similar products?"
            },
            {
                "category": "Comparison",
                "question": f"What makes {product.product_name} different from competitors?"
            }
        ])
        
        # Technical questions
        questions.append({
            "category": "Technical",
            "question": f"What is the {product.concentration}?"
        })
        
        return questions
    
    def get_output(self) -> Dict:
        """Return agent metadata"""
        return {
            "agent": self.name,
            "responsibility": "Generate categorized user questions from product data"
        }
