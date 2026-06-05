from services.gemini_service import generate_content

# Reade a file from prompt
def load_prompt():
    with open("prompts/improve_post.txt") as file:
        return file.read()

def review_post(post: str):

    if not post.strip():
        raise ValueError("Post cannot be empty.")

    prompt_template = load_prompt()

    final_prompt = prompt_template.format(post=post)

    response = generate_content(final_prompt)

    return response