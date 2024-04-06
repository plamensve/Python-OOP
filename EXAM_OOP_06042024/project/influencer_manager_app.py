from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER = {'PremiumInfluencer': PremiumInfluencer, 'StandardInfluencer': StandardInfluencer}
    VALID_CAMPAIGN = {'HighBudgetCampaign': HighBudgetCampaign, 'LowBudgetCampaign': LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER:
            return f"{influencer_type} is not an allowed influencer type."
        try:
            cur_user = next(filter(lambda u: u.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            new_influencer = self.VALID_INFLUENCER[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN:
            return f"{campaign_type} is not a valid campaign type."
        try:
            curr_campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            new_campaign = self.VALID_CAMPAIGN[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(new_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            curr_inf = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            curr_campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        result_eligibility = curr_campaign.check_eligibility(curr_inf.engagement_rate)
        if not result_eligibility:
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment_for_influencer = curr_inf.calculate_payment(curr_campaign)
        if payment_for_influencer > 0.0:
            curr_campaign.approved_influencers.append(curr_inf)
            curr_campaign.budget -= payment_for_influencer
            curr_inf.campaigns_participated.append(curr_campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_followers_dict = {}

        for campaign in self.campaigns:
            if campaign.approved_influencers:
                total_followers = 0
                for influencer in campaign.approved_influencers:
                    total_followers += influencer.reached_followers(campaign.__class__.__name__)
                total_followers_dict[campaign] = total_followers

        return total_followers_dict

    def influencer_campaign_report(self, username: str):
        try:
            curr_user = next(filter(lambda u: u.username == username, self.influencers))
            if not curr_user.campaigns_participated:
                return f"{username} has not participated in any campaigns."
            message = f"{curr_user.__class__.__name__} :) {username} :) participated in the following campaigns:\n"
            list_with_campaings = []
            for campaign in curr_user.campaigns_participated:
                list_with_campaings.append(f"  - Campaign ID: {campaign.campaign_id}, "
                                           f"Brand: {campaign.brand}, "
                                           f"Reached followers: {curr_user.reached_followers(campaign.__class__.__name__)}")
            message += '\n'.join(list_with_campaings)
            return message
        except StopIteration:
            pass

    def campaign_statistics(self):
        message = f"$$ Campaign Statistics $$\n"
        current_campaign = []
        for campaign in self.campaigns:
            current_campaign.append(campaign)

        sorted_campaign_by_approved_influencers = sorted(current_campaign, key=lambda i: (len(i.approved_influencers), -i.budget))
        info_list = []
        total_reached_followers = 0

        for camp in sorted_campaign_by_approved_influencers:
            followers_info = [influencer.reached_followers(camp.__class__.__name__) for influencer in camp.approved_influencers]
            total = 0
            for info in followers_info:
                total += info
            info_list.append(f"  * Brand: {camp.brand}, "
                             f"Total influencers: {len(camp.approved_influencers)}, "
                             f"Total budget: ${camp.budget:.2f}, "
                             f"Total reached followers: {int(total)}")
        message += '\n'.join(info_list)
        return message