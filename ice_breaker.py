from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import sys
print("Python path === ")
print(sys.executable)

information = """
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. He is the founder, chairman, CEO and chief technology officer of SpaceX; the angel investor, CEO and product architect of Tesla, Inc.; the owner and CTO of Twitter; the founder of the Boring Company; the co-founder of Neuralink and OpenAI; and the president of the Musk Foundation. Musk is the wealthiest person in the world, with an estimated net worth of US$239 billion as of July 2023, according to the Bloomberg Billionaires Index, and $248.8 billion according to Forbes's Real Time Billionaires list, primarily from his ownership stakes in Tesla and SpaceX.[4][5][6]

Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before moving to Canada aged 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University in Kingston, Ontario, and two years after that transferred to the University of Pennsylvania, where he received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University. After two days, he dropped out and, with his brother Kimbal, co-founded the online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and with $12 million of the money he made, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.
"""

if __name__ == '__main__':
    print("Hello Amit Langchain!")
    # print(os.environ['OPENAI_API_KEY'])

    summery_template = """
        given the informaiton {information} about a perdon from I want you to create:
        1. a shot summary
        2. two interesting facts about them
     """
    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summery_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
