from ollama_helper import generate
from prompts import company_analysis_prompt


def analyze_company(company):

    prompt = company_analysis_prompt(company)

    response = generate(prompt)

    return response