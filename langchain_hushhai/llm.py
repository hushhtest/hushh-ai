from enum import Enum
import os
from langchain_openai import ChatOpenAI

class HushhAIModel(Enum):
    LLAMA32_3B = "llama32-3b"
    QWEN25_CODER_7B_INSTRUCT = "qwen25-coder-7b-instruct"

    def __str__(self):
        return self.value


class HushhAI(ChatOpenAI):
    def __init__(self, model_slug: HushhAIModel, **kwargs):
        """
        Initializes HushhAI class with a dynamic model slug and any additional args.
        
        Args:
            model_slug (str): The model identifier to use with the API.
            **kwargs: Other keyword arguments to pass to the ChatOpenAI initializer.
        """
        if not isinstance(model_slug, HushhAIModel):
            raise ValueError(f"Invalid model_slug: {model_slug}. Must be an instance of HushhAIModel Enum.")
        
        # Dynamically set the API URL based on the model slug
        base_url = f"https://{model_slug}.hushh-garage.store/v1"
        
        # Pass the dynamically generated URL to the parent class constructor
        super().__init__(base_url=base_url, api_key="dummy", **kwargs)