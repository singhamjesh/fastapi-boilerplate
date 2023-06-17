import os
import logging
from typing import Dict, List, Optional, Any
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from src.utils.decorators import timing_decorator, log_io_decorator
from src.utils.promptBuilder import promptToGrabAmount

logger = logging.getLogger(__name__)


@log_io_decorator
@timing_decorator
def getOpenAIResponse(jpgText):
    llm = OpenAI(openai_api_key=os.environ.get(
        'OPENAI_API_KEY'), temperature=0)
    prompt = promptToGrabAmount()
    chain = LLMChain(llm=llm, prompt=prompt)
    finalResult = chain.run(jpgText)
    return finalResult
