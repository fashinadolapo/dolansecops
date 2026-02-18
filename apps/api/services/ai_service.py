from openai import OpenAI
client = OpenAI(api_key="YOUR_OPENAI_KEY")

def generate_ai_fix(repo_name: str, file_path: str, user):
    """
    Generate a patch suggestion using LLM
    """
    prompt = f"Generate a secure fix for {file_path} in repo {repo_name}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
