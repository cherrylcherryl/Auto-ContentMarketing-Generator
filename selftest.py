from chat.chat import LLMSequentialChatModel


model = LLMSequentialChatModel()

res = model.auto_create_content("print on demain", "facebook")
print(res)