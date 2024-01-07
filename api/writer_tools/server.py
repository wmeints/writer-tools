from typing import Annotated

from fastapi import Body, FastAPI

from writer_tools.requests import (GenerateConclusionRequest,
                                   GenerateIntroductionRequest)
from writer_tools.responses import (ErrorResponse, GenerateConclusionResponse,
                                    GenerateIntroductionResponse)

app = FastAPI(
    title=" Writer Tools API",
    summary="This API is used by the Writer Tools extension to generate content.",
)


@app.post(
    "/api/generate/introduction",
    tags=["generation"],
    responses={500: {"model": ErrorResponse}},
)
def generate_introduction(
    request: Annotated[GenerateIntroductionRequest, Body(embed=False)]
) -> GenerateIntroductionResponse:
    """
    Generate an introduction paragraph for the given content.

    - **content**: The content to generate an introduction for.
    """
    return GenerateIntroductionResponse(introduction="TODO: Implement")


@app.post(
    "/api/generate/conclusion",
    tags=["generation"],
    responses={500: {"model": ErrorResponse}},
)
def generate_conclusion(
    request: Annotated[GenerateConclusionRequest, Body(embed=False)]
) -> GenerateConclusionResponse:
    """
    Generate a conclusion paragraph for the given content.

    - **content**: The content to generate a conclusion for.
    """
    return GenerateConclusionResponse(conclusion="TODO: Implement")
