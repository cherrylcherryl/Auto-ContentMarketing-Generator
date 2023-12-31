class PromptConfig:
    def __init__(self):
        self.constraints =  [
            '~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.',
            'If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.',
            'No user assistance',
            'Exclusively use the commands listed below e.g. command_name'
        ]
        self.resources = [
            'Internet access for searches and information gathering.',
            'Long Term memory management.',
            'GPT-3.5 powered Agents for delegation of simple tasks.',
            'File output.'
        ]
        self.performance_evaluations = [
            'Continuously review and analyze your actions to ensure you are performing to the best of your abilities.',
            'Constructively self-criticize your big-picture behavior constantly.',
            'Reflect on past decisions and strategies to refine your approach.',
            'Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.'
        ]