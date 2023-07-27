from chat.dynamicchat import LLMDynamicChat


model = LLMDynamicChat()

res = model.auto_create_content("print on demain", "facebook")
print(res)