from typing import Annotated

from fastapi import Body, FastAPI

from writer_tools.requests import GenerateConclusionRequest, GenerateIntroductionRequest
from writer_tools.responses import (
    ErrorResponse,
    GenerateConclusionResponse,
    GenerateIntroductionResponse,
)
from writer_tools import languagemodel

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
    result = languagemodel.generate_introduction(request.content)
    return GenerateIntroductionResponse(introduction=result)


@app.post(
    "/api/generate/conclusion",
    tags=["generation"],
    responses={500: {"model": ErrorResponse}},
)
def generate_conclusion(
    request: Annotated[GenerateConclusionRequest, Body(embed=False)]
) -> GenerateConclusionResponse:
    result = languagemodel.generate_conclusion(request.content)
    return GenerateConclusionResponse(conclusion=result)
