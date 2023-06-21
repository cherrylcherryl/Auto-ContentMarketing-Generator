from prompts.generator import PromptGenerator
from config.prompt_config import PromptConfig

DEFAULT_TRIGGERING_PROMPT = "Determine exactly one command to use, and respond using the JSON schema specified previously:"


def build_default_prompt_generator() -> PromptGenerator:
    prompt_generator = PromptGenerator()

    prompt_config = PromptConfig()

    for constraint in prompt_config.constraints:
        prompt_generator.add_constraint(constraint)

    for resource in prompt_config.resources:
        prompt_generator.add_resource(resource)

    for performance_evaluation in prompt_config.performance_evaluations:
        prompt_generator.add_performance_evaluation(performance_evaluation)

    return prompt_generator
