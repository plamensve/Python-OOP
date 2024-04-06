from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        campaign_budget = campaign.budget
        payment_for_influencer = campaign_budget * self.INITIAL_PAYMENT
        return float(payment_for_influencer)

    def reached_followers(self, campaign_type: str):
        if campaign_type == 'HighBudgetCampaign':
            result = (self.followers * self.engagement_rate) * 1.2
            return int(result)

        elif campaign_type == 'LowBudgetCampaign':
            result = (self.followers * self.engagement_rate) * 0.9
            return int(result)
