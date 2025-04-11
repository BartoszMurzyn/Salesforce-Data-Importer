import pandas as pd
from accounts import  create_account
from contacts import merge_contact_data, create_contacts
from opportunities import process_opportunity_data, create_opportunities


def main():
    #Creating Accounts
    result = create_account('accounts.csv')


    #Creating Contacts
    raw_contacts = pd.read_csv('contacts.csv')
    processed_contacts = merge_contact_data(result, raw_contacts)
    contact_result = create_contacts(processed_contacts)
    contact_result.to_csv('contacts_with_ids.csv', index=False)

    #Creating Opportunities
    raw_opportunities = pd.read_csv('opportunities.csv')
    processed_opportunities = process_opportunity_data(result,raw_opportunities)
    opportunities_result = create_opportunities(processed_opportunities)
    opportunities_result.to_csv('opportunities_with_ids.csv', index=False)

if __name__ == '__main__':
    main()