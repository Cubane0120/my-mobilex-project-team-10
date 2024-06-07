from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):
    won_situation: str = Field(
        description='상황을 설명하고, 그 상황에서 최선의 긍정을 찾아봅시다',
        default='연습이 끝나고 물을 마시려는데, 물이 절반 남아있다.',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )

class OutputModel(BaseModel):
    output: str = Field(
        description='원영적 사고 : ',
    )