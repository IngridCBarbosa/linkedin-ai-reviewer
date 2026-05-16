import typer
from rich import print
from services import gemini_service

app = typer.Typer()

# Reade a file from prompt
def load_prompt():
    with open("prompts/improve_post.txt") as file:
        return file.read()

@app.command()
def review():
    post = typer.prompt("[green] Paste your text to post here: ")

    prompt_template = load_prompt()
    final_prompt = prompt_template.format(post=post)

    print("\n[green]Prompt loaded:[/green]")
    print(final_prompt)

    result = gemini_service.generate_content(final_prompt)

    print("[green] Result:")
    print(result)

if __name__ == "__main__":
    app()