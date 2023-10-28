import os
import pandas as pd

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent


def ai(inprom):

    input_data = inprom

    ####################################################################
    #openai 키 설정
    os.environ["OPENAI_API_KEY"] = "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"

    #csv 파일 업로드
    path = "./data/llast_data.csv"
    evaluate = pd.read_csv(path)

    #객체 생성
    agent = create_csv_agent(ChatOpenAI(temperature=0, model= "gpt-3.5-turbo-0613"),path,verbose=True, agent_type = AgentType.OPENAI_FUNCTIONS)

    #일차적 csvOpenai
    output = agent.run(f"{input_data}")

    ######################################################################

    return output