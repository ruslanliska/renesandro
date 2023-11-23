from __future__ import annotations

from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain.schema import SystemMessage
from renesandro.src.config import settings
from renesandro.src.openai_client.enums import TextsListResult
from renesandro.src.texts.schemas import TextDescriptionSchema

OPENAI_MODEL = 'gpt-4-1106-preview'


class OpenAIClient:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY, model_name=OPENAI_MODEL,
        )

    def generate_texts(self, description: TextDescriptionSchema):
        parser = PydanticOutputParser(pydantic_object=TextsListResult)
        format_instructions = parser.get_format_instructions()
        messages = [
            SystemMessage(
                content='You are a helpful book writer. You will help me in generating texts for marketing purposes. '
                        'I will provide you description of texts, product description, type, and auditory description. '
                        'You can create names, whatever, just to make this real.ß',
            ),
            HumanMessage(
                content=f"""Here is general description for texts: {description.description}
                            Please, generate for me {description.texts_quantity} texts for {description.auditory_description} auditory.
                            Each text must be as a {description.text_type}.
                            And maximum amount of characters in each text must be lower than {description.max_characters}
                            \n{format_instructions}""",
            ),
        ]

        prompt = ChatPromptTemplate(
            messages=messages,
        )
        _input = prompt.format_prompt()

        output = self.llm.predict_messages(_input.to_messages())
        my_output = parser.parse(output.content)
        return my_output.model_dump()['texts']
