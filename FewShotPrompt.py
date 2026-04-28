
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt = PromptTemplate.from_template(
    "单词：{word}, 反义词：{antonym}"
)

example_datas = [
    {"word": "good", "antonym": "bad"},
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
    {"word": "big", "antonym": "small"},
    {"word": "fast", "antonym": "slow"}
]

few_shot_prompt = FewShotPromptTemplate(
    example_prompt=prompt,
    examples=example_datas,
    prefix="请给出单词的反义词",
    suffix="基于前面实例，{input_word}的反义词是什么？",
    input_variables=["input_word"]
)

prompt_text = few_shot_prompt.invoke(input={"input_word": "happy"}).to_string()


model = Tongyi(model="qwen-max")
print(model.invoke(input=prompt_text))
