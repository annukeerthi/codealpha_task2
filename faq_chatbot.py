# faq_chatbot.py
import spacy
from collections import defaultdict

def load_faqs():
    return {
        "What is your return policy?": "You can return any product within 30 days of purchase with a valid receipt.",
        "How can I track my order?": "You can track your order using the tracking number sent to your email after purchase.",
        "Do you offer international shipping?": "Yes, we offer international shipping. Shipping charges may apply based on your location.",
        "What payment methods do you accept?": "We accept credit/debit cards, PayPal, and Apple Pay."
    }

def find_best_match(user_question, faqs, nlp):
    user_doc = nlp(user_question.lower())
    best_match = None
    best_similarity = 0.0
    
    for question, answer in faqs.items():
        question_doc = nlp(question.lower())
        similarity = user_doc.similarity(question_doc)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = answer
    
    return best_match if best_similarity > 0.5 else "I'm sorry, I don't have an answer for that."

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_md")
    faqs = load_faqs()
    
    print("FAQ Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = find_best_match(user_input, faqs, nlp)
        print("Bot:", response)
