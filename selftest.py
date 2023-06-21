from prompts.auto_generator import AutoPromptGenerator

generator = AutoPromptGenerator("data")

output = generator.generate_dynamic_analysis_prompt_specific_domain("market analysis")

print(output)