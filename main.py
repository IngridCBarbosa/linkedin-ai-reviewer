import typer
from rich import print

app = typer.Typer()

@app.command()
def review():
    print("[blue]LinkedIn AI Reviewer is running...[/blue]")

if __name__ == "__main__":
    app()