"""
Product data model - Internal representation of product information
"""
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Product:
    """Internal product data model"""
    product_name: str
    concentration: str
    suitable_for: str
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: Optional[str]
    price: str
    
    def to_dict(self) -> dict:
        """Convert product to dictionary"""
        return {
            "product_name": self.product_name,
            "concentration": self.concentration,
            "suitable_for": self.suitable_for,
            "key_ingredients": self.key_ingredients,
            "benefits": self.benefits,
            "how_to_use": self.how_to_use,
            "side_effects": self.side_effects,
            "price": self.price
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Product':
        """Create product from dictionary"""
        return cls(
            product_name=data.get("product_name", ""),
            concentration=data.get("concentration", ""),
            suitable_for=data.get("suitable_for", ""),
            key_ingredients=data.get("key_ingredients", []),
            benefits=data.get("benefits", []),
            how_to_use=data.get("how_to_use", ""),
            side_effects=data.get("side_effects"),
            price=data.get("price", "")
        )
