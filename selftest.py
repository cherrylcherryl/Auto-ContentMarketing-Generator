from prompts.auto_generator import AutoMarketAnalysisPromptGenerator

generator = AutoMarketAnalysisPromptGenerator("data")

output = generator.generate_dynamic_prompt("market analysis")

print(output)