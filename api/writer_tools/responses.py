from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    error_message: str = Field(
        title="The error message", description="The error message", alias="errorMessage"
    )


class GenerateConclusionResponse(BaseModel):
    conclusion: str = Field(
        title="The conclusion for the article",
        description="The conclusion for the article",
        default=None,
    )


class GenerateIntroductionResponse(BaseModel):
    introduction: str = Field(
        title="The introduction of the article",
        description="The introduction of the article",
        default=None,
    )
