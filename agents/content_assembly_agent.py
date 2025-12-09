"""
Content Assembly Agent - Assembles content pages using templates and blocks
"""
from typing import Dict
from models.product import Product
from templates.template_engine import TemplateEngine
import blocks.content_blocks as blocks


class ContentAssemblyAgent:
    """Agent responsible for assembling content pages"""
    
    def __init__(self):
        self.name = "ContentAssemblyAgent"
        self.template_engine = TemplateEngine()
    
    def assemble_faq_page(self, product: Product, questions: list, answers: list) -> Dict:
        """
        Assemble FAQ page using template
        
        Args:
            product: Product model
            questions: List of questions
            answers: List of answers
            
        Returns:
            Structured FAQ page data
        """
        return self.template_engine.render_template(
            "faq",
            product=product,
            questions=questions,
            answers=answers
        )
    
    def assemble_product_page(self, product: Product) -> Dict:
        """
        Assemble product page using template and content blocks
        
        Args:
            product: Product model
            
        Returns:
            Structured product page data
        """
        # Generate content blocks
        overview = blocks.generate_overview_block(product)
        benefits = blocks.generate_benefits_block(product)
        ingredients = blocks.generate_ingredients_block(product)
        usage = blocks.extract_usage_block(product)
        safety = blocks.extract_safety_block(product)
        pricing = blocks.generate_price_block(product)
        
        # Render template with blocks
        return self.template_engine.render_template(
            "product",
            product=product,
            overview=overview,
            benefits=benefits,
            ingredients=ingredients,
            usage=usage,
            safety=safety,
            pricing=pricing
        )
    
    def assemble_comparison_page(self, product_a: Product, product_b: Product) -> Dict:
        """
        Assemble comparison page using template and comparison blocks
        
        Args:
            product_a: First product
            product_b: Second product
            
        Returns:
            Structured comparison page data
        """
        # Generate comparison blocks
        ingredients_comp = blocks.compare_ingredients_block(product_a, product_b)
        benefits_comp = blocks.compare_benefits_block(product_a, product_b)
        price_comp = blocks.compare_price_block(product_a, product_b)
        
        # Render template with comparison blocks
        return self.template_engine.render_template(
            "comparison",
            product_a=product_a,
            product_b=product_b,
            ingredients_comparison=ingredients_comp,
            benefits_comparison=benefits_comp,
            price_comparison=price_comp
        )
    
    def get_output(self) -> Dict:
        """Return agent metadata"""
        return {
            "agent": self.name,
            "responsibility": "Assemble content pages using templates and content blocks"
        }
