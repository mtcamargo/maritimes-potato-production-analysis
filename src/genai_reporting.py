from dotenv import load_dotenv
import os
from openai import OpenAI 

load_dotenv()  # loads variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_agriculture_report(province, year, stats_dict):
    """
    Generates a professional agricultural climate & disease risk report.
    """

    prompt = f"""
    You are an agricultural risk analyst.

    Generate a professional annual potato production report
    for {province} in {year} based on the following statistics:

    {stats_dict}

    Include:
    - Production performance summary
    - Climate impact interpretation
    - Disease risk analysis
    - Recommendations for farmers
    - Policy-level suggestions

    Keep tone professional and evidence-based.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional agricultural data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content