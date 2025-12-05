"""
RAG Food System Test Queries
=============================
Comprehensive test suite with 15 diverse queries to validate the RAG system's ability
to search, retrieve, and synthesize information about food items based on semantic similarity.

Categories:
1. Specific Dish Inquiries (3 queries) - Testing direct food recognition
2. Nutritional Questions (3 queries) - Testing protein/fiber/omega-3 searches
3. Cultural Cuisine Queries (3 queries) - Testing regional food knowledge
4. Dietary Restriction Searches (3 queries) - Testing vegetarian/vegan/gluten-free filters
5. Cooking Method Questions (3 queries) - Testing grilling/braising/stirring methods
"""

# SPECIFIC DISH INQUIRIES
queries_specific_dishes = [
    "Tell me about Haleem and its cultural significance in Lahore",
    "What are the main ingredients in Karahi Gosht?",
    "Describe the preparation method for Seekh Kebab"
]

# NUTRITIONAL QUESTIONS  
queries_nutritional = [
    "Which foods have high protein content and are suitable for muscle building?",
    "What dishes are rich in fiber and good for digestive health?",
    "Show me foods high in omega-3 fatty acids for heart health"
]

# CULTURAL CUISINE QUERIES
queries_cultural = [
    "What are authentic Pakistani dishes from Lahore?",
    "Tell me about traditional European cooking methods",
    "What is the significance of Asian noodle dishes?"
]

# DIETARY RESTRICTION SEARCHES
queries_dietary = [
    "Which foods are completely vegetarian or vegan?",
    "What gluten-free options are available?",
    "Show me low-calorie but nutritious food options"
]

# COOKING METHOD QUESTIONS
queries_cooking_methods = [
    "What dishes use charcoal grilling as the primary cooking method?",
    "Which foods require braising or slow-cooking techniques?",
    "What dishes are made using constant stirring or specific pan techniques?"
]

# Combined test suite
all_queries = (
    queries_specific_dishes +
    queries_nutritional +
    queries_cultural +
    queries_dietary +
    queries_cooking_methods
)

if __name__ == "__main__":
    print("RAG Food System Test Queries")
    print("=" * 50)
    print(f"Total queries: {len(all_queries)}")
    print("\nQuery Categories:")
    print(f"- Specific Dishes: {len(queries_specific_dishes)}")
    print(f"- Nutritional: {len(queries_nutritional)}")
    print(f"- Cultural: {len(queries_cultural)}")
    print(f"- Dietary: {len(queries_dietary)}")
    print(f"- Cooking Methods: {len(queries_cooking_methods)}")
