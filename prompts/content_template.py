from langchain.prompts import PromptTemplate
from viewmodel.model import CompanyAnalysis
from utils.prompt_utils import add_analysis_info, add_language

class ContentGeneratorPrompt:
    def __init__(self):
        self.templates =  PromptTemplate(
                input_variables=["company", "socialMedia", "tone"],
                template='''
                    I'm looking for some creative ways to promote our {company} through content marketing and engage our target audience.
                    Write a post in {socialMedia} with {tone} tone style, including hashtag and other additional information that is common on this media.            
                '''
            )

    def get_content_generator_prompt(
            self, 
            companyAnalysis : CompanyAnalysis
    ) -> str:
        base_prompt = self.templates.format(
            company=companyAnalysis.name,
            socialMedia=companyAnalysis.socialMedia,
            tone=companyAnalysis.tone
        )
        base_prompt = add_analysis_info(
            market_analysis=companyAnalysis.market_analysis,
            competitor=companyAnalysis.competitor,
            key_selling_point=companyAnalysis.key_selling_point,
            base_prompt=base_prompt
        )
        base_prompt = add_language(
            language=companyAnalysis.language,
            base_prompt=base_prompt
        )
        return base_prompt
