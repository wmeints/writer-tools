import typer
import uvicorn
from typing_extensions import Annotated


def main(
    address: Annotated[str, typer.Option(help="The address to bind to")] = "0.0.0.0",
    port: Annotated[int, typer.Option(help="The port to bind to")] = 5000,
):
    uvicorn.run("writer_tools.server:app", host=address, port=port)


if __name__ == "__main__":
    typer.run(main)
