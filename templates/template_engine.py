"""
Template Engine - Defines and manages page templates
"""
from typing import Dict, List, Callable, Any
from models.product import Product


class Template:
    """Base template class"""
    
    def __init__(self, name: str):
        self.name = name
        self.fields = {}
        self.rules = []
        
    def add_field(self, field_name: str, block_function: Callable, dependencies: List[str] = None):
        """Add a field to the template with its content block function"""
        self.fields[field_name] = {
            "block_function": block_function,
            "dependencies": dependencies or []
        }
        
    def add_rule(self, rule: Callable):
        """Add a formatting/validation rule"""
        self.rules.append(rule)
        
    def render(self, **kwargs) -> Dict[str, Any]:
        """Render the template with provided data"""
        result = {
            "template": self.name,
            "content": {}
        }
        
        # Execute content blocks for each field
        for field_name, field_config in self.fields.items():
            block_function = field_config["block_function"]
            result["content"][field_name] = block_function(**kwargs)
        
        # Apply rules
        for rule in self.rules:
            result = rule(result)
            
        return result


class FAQTemplate(Template):
    """FAQ page template"""
    
    def __init__(self):
        super().__init__("FAQ")
        
    def render(self, product: Product, questions: List[Dict], answers: List[str]) -> Dict:
        """
        Render FAQ page
        
        Args:
            product: Product model
            questions: List of question dictionaries
            answers: List of answers corresponding to questions
            
        Returns:
            Structured FAQ page data
        """
        faq_items = []
        
        # Take at least 5 questions for FAQ
        for i, q in enumerate(questions[:min(len(questions), len(answers))]):
            faq_items.append({
                "category": q.get("category", "General"),
                "question": q.get("question", ""),
                "answer": answers[i] if i < len(answers) else ""
            })
        
        return {
            "page_type": "faq",
            "product_name": product.product_name,
            "faq_count": len(faq_items),
            "faqs": faq_items,
            "metadata": {
                "generated_from": "FAQ Template",
                "categories": list(set([item["category"] for item in faq_items]))
            }
        }


class ProductPageTemplate(Template):
    """Product description page template"""
    
    def __init__(self):
        super().__init__("ProductPage")
        
    def render(self, product: Product, overview: Dict, benefits: Dict, 
               ingredients: Dict, usage: Dict, safety: Dict, pricing: Dict) -> Dict:
        """
        Render product page
        
        Args:
            product: Product model
            overview: Overview block data
            benefits: Benefits block data
            ingredients: Ingredients block data
            usage: Usage block data
            safety: Safety block data
            pricing: Pricing block data
            
        Returns:
            Structured product page data
        """
        return {
            "page_type": "product",
            "product_name": product.product_name,
            "sections": {
                "overview": overview,
                "benefits": benefits,
                "ingredients": ingredients,
                "usage": usage,
                "safety": safety,
                "pricing": pricing
            },
            "metadata": {
                "generated_from": "Product Page Template",
                "section_count": 6
            }
        }


class ComparisonPageTemplate(Template):
    """Comparison page template"""
    
    def __init__(self):
        super().__init__("ComparisonPage")
        
    def render(self, product_a: Product, product_b: Product,
               ingredients_comparison: Dict, benefits_comparison: Dict,
               price_comparison: Dict) -> Dict:
        """
        Render comparison page
        
        Args:
            product_a: First product
            product_b: Second product
            ingredients_comparison: Ingredients comparison block
            benefits_comparison: Benefits comparison block
            price_comparison: Price comparison block
            
        Returns:
            Structured comparison page data
        """
        return {
            "page_type": "comparison",
            "products": {
                "product_a": {
                    "name": product_a.product_name,
                    "price": product_a.price,
                    "key_spec": product_a.concentration,
                    "suitable_for": product_a.suitable_for
                },
                "product_b": {
                    "name": product_b.product_name,
                    "price": product_b.price,
                    "key_spec": product_b.concentration,
                    "suitable_for": product_b.suitable_for
                }
            },
            "comparisons": {
                "ingredients": ingredients_comparison,
                "benefits": benefits_comparison,
                "pricing": price_comparison
            },
            "metadata": {
                "generated_from": "Comparison Page Template",
                "comparison_categories": ["ingredients", "benefits", "pricing"]
            }
        }


class TemplateEngine:
    """Template engine for managing and rendering templates"""
    
    def __init__(self):
        self.templates = {
            "faq": FAQTemplate(),
            "product": ProductPageTemplate(),
            "comparison": ComparisonPageTemplate()
        }
    
    def get_template(self, template_name: str) -> Template:
        """Get template by name"""
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found")
        return self.templates[template_name]
    
    def render_template(self, template_name: str, **kwargs) -> Dict:
        """Render a template with provided data"""
        template = self.get_template(template_name)
        return template.render(**kwargs)
