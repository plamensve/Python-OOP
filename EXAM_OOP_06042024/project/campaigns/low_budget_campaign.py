from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    INITIAL_BUDGET = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.INITIAL_BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        needed_engagement_rate = self.required_engagement * 0.9
        if engagement_rate >= needed_engagement_rate:
            return True
        return False
