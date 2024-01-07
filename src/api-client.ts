import axios from "axios";
import { isError } from "util";

interface ErrorResponse {
  errorMessage: string;
}

interface GenerateConclusionResponse {
  conclusion: string;
}

interface GenerateIntroductionResponse {
  introduction: string;
}

function isErrorResponse<T>(
  response: T | ErrorResponse
): response is ErrorResponse {
  return (response as ErrorResponse).errorMessage !== undefined;
}

export class ApiClient {
  private baseUrl: string;
  private apiKey: string;

  constructor(baseUrl: string, apiKey: string) {
    this.baseUrl = baseUrl;
    this.apiKey = apiKey;
  }

  async generateConclusion(content: string): Promise<string> {
    const response = await axios.post<
      GenerateConclusionResponse | ErrorResponse
    >(`${this.baseUrl}/api/generate/conclusion`, {
      content: content,
    });

    if (isErrorResponse(response.data)) {
      throw new Error(response.data.errorMessage);
    }

    return response.data.conclusion;
  }

  async generateIntroduction(content: string): Promise<string> {
    const response = await axios.post<
      GenerateIntroductionResponse | ErrorResponse
    >(`${this.baseUrl}/api/generate/introduction`, { content: content });

    if (isErrorResponse(response.data)) {
      throw new Error(response.data.errorMessage);
    }

    return response.data.introduction;
  }
}
