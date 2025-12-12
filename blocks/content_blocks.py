"""
Content logic blocks - Reusable functions for transforming product data into content
"""
from typing import List, Dict
from models.product import Product


def _is_valid_value(value: str) -> bool:
    if value is None:
        return False
    try:
        s = str(value).strip()
    except Exception:
        return False
    if s == "":
        return False
    if s.lower() in ("n/a", "na", "none", "null"):
        return False
    return True


def generate_benefits_block(product: Product) -> Dict[str, any]:
    """
    Generate benefits content block
    
    Args:
        product: Product model
        
    Returns:
        Dictionary with formatted benefits information
    """
    return {
        "title": "Key Benefits",
        "benefits": product.benefits,
        "summary": f"{product.product_name} offers multiple benefits including {', '.join(product.benefits[:-1])} and {product.benefits[-1]}." if len(product.benefits) > 1 else f"{product.product_name} provides {product.benefits[0]}."
    }


def extract_usage_block(product: Product) -> Dict[str, str]:
    """
    Extract usage instructions block
    
    Args:
        product: Product model
        
    Returns:
        Dictionary with usage information
    """
    return {
        "title": "How to Use",
        "instructions": product.how_to_use,
        "recommendation": f"For best results: {product.how_to_use}"
    }


def extract_safety_block(product: Product) -> Dict[str, str]:
    """
    Extract safety and side effects block
    
    Args:
        product: Product model
        
    Returns:
        Dictionary with safety information
    """
    return {
        "title": "Safety Information",
        "side_effects": product.side_effects if product.side_effects else "No known side effects",
        "warning": f"Note: {product.side_effects}" if product.side_effects else "Safe for use as directed"
    }


def generate_ingredients_block(product: Product) -> Dict[str, any]:
    """
    Generate ingredients/components block
    
    Args:
        product: Product model
        
    Returns:
        Dictionary with ingredient information
    """
    return {
        "title": "Key Components",
        "ingredients": product.key_ingredients,
        "description": f"Contains {len(product.key_ingredients)} key components: {', '.join(product.key_ingredients)}"
    }


def generate_price_block(product: Product) -> Dict[str, str]:
    """
    Generate pricing block
    
    Args:
        product: Product model
        
    Returns:
        Dictionary with pricing information
    """
    return {
        "title": "Pricing",
        "price": product.price,
        "display": f"Available at {product.price}"
    }


def compare_ingredients_block(product_a: Product, product_b: Product) -> Dict[str, any]:
    """
    Compare ingredients between two products
    
    Args:
        product_a: First product
        product_b: Second product
        
    Returns:
        Dictionary with comparison data
    """
    common = set(product_a.key_ingredients) & set(product_b.key_ingredients)
    unique_a = set(product_a.key_ingredients) - set(product_b.key_ingredients)
    unique_b = set(product_b.key_ingredients) - set(product_a.key_ingredients)
    
    return {
        "common_ingredients": list(common),
        "unique_to_a": list(unique_a),
        "unique_to_b": list(unique_b),
        "summary": f"{len(common)} common components, {len(unique_a)} unique to {product_a.product_name}, {len(unique_b)} unique to {product_b.product_name}"
    }


def compare_benefits_block(product_a: Product, product_b: Product) -> Dict[str, any]:
    """
    Compare benefits between two products
    
    Args:
        product_a: First product
        product_b: Second product
        
    Returns:
        Dictionary with benefit comparison
    """
    common = set(product_a.benefits) & set(product_b.benefits)
    unique_a = set(product_a.benefits) - set(product_b.benefits)
    unique_b = set(product_b.benefits) - set(product_a.benefits)
    
    return {
        "common_benefits": list(common),
        "unique_to_a": list(unique_a),
        "unique_to_b": list(unique_b),
        "advantage_a": f"{product_a.product_name} additionally provides: {', '.join(unique_a)}" if unique_a else None,
        "advantage_b": f"{product_b.product_name} additionally provides: {', '.join(unique_b)}" if unique_b else None
    }


def compare_price_block(product_a: Product, product_b: Product) -> Dict[str, str]:
    """
    Compare pricing between two products
    
    Args:
        product_a: First product
        product_b: Second product
        
    Returns:
        Dictionary with price comparison
    """
    return {
        f"{product_a.product_name}_price": product_a.price,
        f"{product_b.product_name}_price": product_b.price,
        "comparison": f"{product_a.product_name} is priced at {product_a.price} while {product_b.product_name} is priced at {product_b.price}"
    }


def generate_overview_block(product: Product) -> Dict[str, str]:
    """
    Generate product overview block
    
    Args:
        product: Product model
        
    Returns:
        Dictionary with overview information
    """
    key_spec = product.concentration if _is_valid_value(product.concentration) else None
    if key_spec:
        summary = f"{product.product_name} with {key_spec} is {product.suitable_for}"
    else:
        summary = f"{product.product_name} is {product.suitable_for}"

    result = {
        "title": "Product Overview",
        "name": product.product_name,
        "suitability": product.suitable_for,
        "summary": summary
    }

    if key_spec:
        result["key_spec"] = key_spec

    return result
