from pydantic import BaseModel, Field


class GenerateConclusionRequest(BaseModel):
    content: str = Field(title="The content of the article", default=None)


class GenerateIntroductionRequest(BaseModel):
    content: str = Field(title="The content of the article", default=None)
