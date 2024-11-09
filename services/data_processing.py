import requests
from langchain_core.documents import Document


def data_processing():
    url = "http://makeup-api.herokuapp.com/api/v1/products.json"
    product_data = requests.get(url).json()
    documents = []

    for product in product_data:
        product_colors = ', '.join(
            [color['colour_name'] for color in product['product_colors'] if color.get('colour_name')]
        )
        document = Document(
            id=product["id"],
            page_content=f"{product['name']} {product['description']}",
            metadata={
                'brand': str(product['brand']),
                'name': str(product['name']),
                'price': str(product['price']),
                'price_sign': str(product['price_sign']),
                'description': str(product['description']),
                'category': str(product['category']),
                'product_type': str(product['product_type']),
                'tag_list': ', '.join(product['tag_list']),
                'created_at': str(product['created_at']),
                'updated_at': str(product['updated_at']),
                'product_api_url': str(product['product_api_url']),
                'product_colors': product_colors,
            }
        )
        documents.append(document)

    return documents
