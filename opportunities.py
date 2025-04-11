import pandas as pd
from config import sf

STAGE_MAPPING = {
    'demo': 'Propose',
    'lost': 'Closed Lost',
    'won': 'Closed Won',
    'negotiation': 'Negotiate',
    'qualification': 'Qualify',
    'presentation': 'Meet & Present',
    'lead': 'Negotiate'
}


def process_opportunity_data(account_df, opportunity_df):
    """Transform and merge opportunity data"""
    merged = pd.merge(
        account_df[['id', 'Company_id']],
        opportunity_df.replace({'opportunity_stage': STAGE_MAPPING}),
        left_on='id',
        right_on='company'
    )
    merged['close_date'] = pd.to_datetime(merged['close_date']).dt.strftime('%Y-%m-%d')
    return merged


def create_opportunities(processed_df):
    """Create Salesforce opportunities"""
    opportunity_ids = []
    for index, row in processed_df.iterrows():
        opportunity_data = {
            'Name': row['opportunity_name'],
            'StageName': row['opportunity_stage'],
            'CloseDate': row['close_date'],
            'AccountId': row['Company_id'],
            'Amount': row['amount']
        }
        try:
            result = sf.Opportunity.create(opportunity_data)
            opportunity_ids.append(result['id'])
            print(f"Created Opportunity ID: {result['id']}")
        except Exception as e:
            print(f"Opportunity creation error: {e}")
            opportunity_ids.append(None)
    return processed_df.assign(opportunity_id=opportunity_ids)

