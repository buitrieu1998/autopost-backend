import typer
from . import ai, instagram, video

app = typer.Typer(help="AutoPost command line interface")


@app.command()
def generate_image(prompt: str, output: str = "generated.png"):
    """Generate an AI image."""
    ai.generate_image(prompt, filename=output)
    typer.echo(f"Image saved to {output}")


@app.command()
def post(prompt: str, caption: str):
    """Generate an image from a prompt and post it to Instagram."""
    path = ai.generate_image(prompt)
    instagram.post_image_to_instagram(path, caption)
    typer.echo("Posted to Instagram")


@app.command()
def bulk_edit(input_dir: str, output_dir: str, text: str):
    """Edit all videos in a directory by adding overlay text."""
    video.bulk_edit_videos(input_dir, output_dir, text)
    typer.echo("Videos processed")


if __name__ == "__main__":
    app()
