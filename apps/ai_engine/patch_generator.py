import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def generate_patch(file_path: str, vulnerability_desc: str, org_id: str) -> str:
    """
    Generate a secure patch for a vulnerability.
    """
    prompt = f"""
    Org: {org_id}
    File: {file_path}
    Vulnerability: {vulnerability_desc}

    Generate a secure code fix, comment the change, and provide reasoning.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
