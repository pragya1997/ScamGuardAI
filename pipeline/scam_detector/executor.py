#communicating applicaion to the llm which interannly connectcs wth gemini api 


from typing import Optional
from xml.parsers.expat import model
from llm.client import LLMClient
from utils import get_logger

logger = get_logger(__name__)

class LLMExecutor:
    """Executes prompts using LLM client and processes responses."""

    def __init__(self, model: Optional[str] = None)-> None:
        """
        Initialize the LLM executor.
        """

        self.llm = LLMClient(model_name=model) if model else LLMClient()
        logger.info(f"LLM Executor initialized with model: {self.llm.model_name}")

    def execute(self, prompt: str) -> str:
        """
        Execute a prompt and return the response.
        Args:
            prompt (str): The prompt to send to the LLM.
        Returns:
            str: The response from the LLM.
        Raises:
            Exception: If the LLM call fails after retries.
        """
        logger.info(f"Executing LLM with prompt length :{len(prompt)}")
        try:
            response = self.llm.call(prompt)
            logger.info(f"LLM executing successfull, response length: {len(response)}")
            return response
        except Exception as e:
            logger.error(f"LLM execution failed: {e}")
            raise