"""
Data Parser Agent - Responsible for parsing and validating product data
"""
import json
from typing import Dict
from models.product import Product


class DataParserAgent:
    """Agent responsible for parsing raw product data into internal model"""
    
    def __init__(self):
        self.name = "DataParserAgent"
    
    def parse_from_file(self, filepath: str) -> Product:
        """
        Parse product data from JSON file
        
        Args:
            filepath: Path to JSON file containing product data
            
        Returns:
            Product: Validated product model
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        return self.parse(raw_data)
    
    def parse(self, raw_data: Dict) -> Product:
        """
        Parse and validate raw product data
        
        Args:
            raw_data: Dictionary containing product information
            
        Returns:
            Product: Validated product model
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        # Validate required fields
        required_fields = ["product_name", "price", "benefits"]
        for field in required_fields:
            if field not in raw_data or not raw_data[field]:
                raise ValueError(f"Missing required field: {field}")
        
        # Parse product
        product = Product.from_dict(raw_data)
        
        return product
    
    def get_output(self) -> Dict:
        """Return agent metadata"""
        return {
            "agent": self.name,
            "responsibility": "Parse and validate product data into internal model"
        }
