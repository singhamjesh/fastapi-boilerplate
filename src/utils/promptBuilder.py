from langchain.prompts import PromptTemplate

# Make a prompt for fetch invoice amount
# @params {str} sentence
# @return {str} prompt


def promptToGrabAmount():
    prompt_creation_template = (
        "You are a helpful assistant \n"
        "To extract items and prices from the given text \n"
        "List down in ascending order with the below formate \n"
        "S.N - item name - item unit price * item unit - total price \n"
        "Here is the text:- \n{value}"
    )

    prompt = PromptTemplate(
        input_variables=["value"],
        template=prompt_creation_template,
    )
    return prompt
