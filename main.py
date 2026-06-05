import typer
from rich import print
from services import gemini_service

from core.reviewer import review_post

app = typer.Typer()


@app.command()
def review():
    post = typer.prompt("[green] Paste your text to post here: ")

    try:
        response = review_post(post)
    except Exception as error:
        print(error)

    print("\n[green] Improved LinkedIn Post:[/green]\n")

    print(response)

if __name__ == "__main__":
    app()