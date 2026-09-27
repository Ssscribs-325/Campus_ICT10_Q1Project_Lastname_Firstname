import random
import string

class SKUGenerator:
    def __init__(self):
        self.existing_skus = set()

    def generate_sku(self, category: str, product: str, attribute_x: str, attribute_y: str) -> str:
        cat_code = self._clean(category)[:3]
        prod_code = self._clean(product)[:3]
        x_code = self._clean(attribute_x)[:3]
        y_code = self._clean(attribute_y)[:3]

        base_parts = [cat_code, prod_code, x_code, y_code]
        base_sku = "-".join([p for p in base_parts if p])

        while True:
            suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
            candidate = f"{base_sku}-{suffix}"
            if candidate not in self.existing_skus:
                self.existing_skus.add(candidate)
                return candidate

    def _clean(self, text: str) -> str:
        return "".join(ch for ch in text if ch.isalnum()).upper()

if __name__ == "__main__":
    generator = SKUGenerator()
    sku = generator.generate_sku(
        category="CategoryA", 
        product="ProductB", 
        attribute_x="X", 
        attribute_y="Y"
    )
    print(f"Generated SKU: {sku}")
