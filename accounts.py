import pandas as pd
from config import sf



def create_account(data):
    """Creates SF Accounts from dataframe"""
    df = pd.read_csv(data)
    df['BillingStreet'] = df['billing_street_number'].astype(str) + ' ' + df['billing_street']
    field_mapping = {
        'Phone': 'telephone',
        'BillingStreet': 'BillingStreet',
        'BillingCity': 'billing_city',
        'BillingPostalCode': 'zip',
        'Name': 'company_name',

    }
    company_id = []
    for index, row in df.iterrows():
        account_data = {sf_field: row[csv_column] for sf_field, csv_column in field_mapping.items()}
        try:
            result = sf.Account.create(account_data)
            print(f"Successfully created Account with ID: {result['id']}")
            company_id.append(result['id'])
            print(company_id)
        except Exception as e:
            print(f"Error creating Account for row {index}: {e}")
    print(len(company_id))
    df['Company_id'] = company_id
    df.to_csv('accounts_with_ids.csv',index = False)
    return df
