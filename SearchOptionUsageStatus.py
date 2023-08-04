import pandas as pd
from inf_functions import get_log_column

INFLUENCER_ID = 'id'
INFLUENCER_NAME = 'name'
PRODUCT_LINE = 'product_line_id'
MODELS = 'product_id'
LOCATION = 'location_id'
ASSIGNMENT_STATUS = 'contact_status_id'
PRIMARY_CONTACT = 'primary_user_id'
CONTACT_PERSON = 'contact_user_id'
OUTREACHED_START = 'outreached_start'
OUTREACHED_END = 'outreached_end'
ACCEPTED_START = 'accepted_start'
ACCEPTED_END = 'accepted_end'
PUBLISHED_START = 'published_start'
PUBLISHED_END = 'published_end'
PAGE_NUM = 'page'
MEDIA_TYPE = 'media_type_id'
CATEGORY = 'category_id'
SPECIALTY = 'specialty_id'
SOCIAL_PLATFORM = 'link_site'
PUBLISH_PLATFORM = 'platform_id'

options_count = {
                INFLUENCER_ID: 0,
                INFLUENCER_NAME: 0, 
                PRODUCT_LINE: 0,
                MODELS: 0,
                LOCATION: 0,
                ASSIGNMENT_STATUS: 0,
                PRIMARY_CONTACT: 0,
                CONTACT_PERSON: 0,
                OUTREACHED_START: 0,
                OUTREACHED_END: 0,
                ACCEPTED_START: 0,
                ACCEPTED_END: 0,
                PUBLISHED_START: 0,
                PUBLISHED_END: 0,
                MEDIA_TYPE: 0,
                CATEGORY: 0,
                SPECIALTY: 0,
                SOCIAL_PLATFORM: 0,
                PUBLISH_PLATFORM: 0 }

options_name = {
                INFLUENCER_ID: 'Serial Number',
                INFLUENCER_NAME: 'Name', 
                PRODUCT_LINE: 'Product Line',
                MODELS: 'Model',
                LOCATION: 'Influenced Country(s)',
                ASSIGNMENT_STATUS: 'Status',
                PRIMARY_CONTACT: 'Primary Contact',
                CONTACT_PERSON: 'Contact Person',
                OUTREACHED_START: 'Outreach Date Range',
                OUTREACHED_END: 'Outreach Date Range',
                ACCEPTED_START: 'Accept Date Range',
                ACCEPTED_END: 'Accept Date Range',
                PUBLISHED_START: 'Post Date Range',
                PUBLISHED_END: 'Post Date Range',
                MEDIA_TYPE: 'Media Type',
                CATEGORY: 'Category',
                SPECIALTY: 'Specialty',
                SOCIAL_PLATFORM: 'Socail Platform',
                PUBLISH_PLATFORM: 'Publish Platform' }


options_default = {
                INFLUENCER_ID: '0',
                INFLUENCER_NAME: 'null', 
                PRODUCT_LINE: '-1',
                MODELS: '',
                LOCATION: '-1',
                ASSIGNMENT_STATUS: '-1',
                PRIMARY_CONTACT: '-1',
                CONTACT_PERSON: '-1',
                OUTREACHED_START: 'null',
                OUTREACHED_END: 'null',
                ACCEPTED_START: 'null',
                ACCEPTED_END: 'null',
                PUBLISHED_START: 'null',
                PUBLISHED_END: 'null',
                PAGE_NUM: '',
                MEDIA_TYPE: '-1',
                CATEGORY: '-1',
                SPECIALTY: '-1',
                SOCIAL_PLATFORM: 'null',
                PUBLISH_PLATFORM: '-1' }

CAMPAIGN_ID = 'id'
CAMPAIGN_REGION = 'region_id'
CAMPAIGN_PRODUCT_LINE = 'product_line_id'
CAMPAIGN_MODELS = 'product_id'
CAMPAIGN_OWNER = 'user_id'
CAMPAIGN_CREATE_START = 'created_start'
CAMPAIGN_CREATE_END = 'created_end'
campaign_option_count = {CAMPAIGN_ID: 0,
                        CAMPAIGN_REGION: 0,
                        CAMPAIGN_PRODUCT_LINE: 0,
                        CAMPAIGN_MODELS: 0,
                        CAMPAIGN_OWNER: 0,
                        CAMPAIGN_CREATE_START: 0,
                        CAMPAIGN_CREATE_END: 0}


campaign_option_name = {CAMPAIGN_ID: 'Campaign Name',
                        CAMPAIGN_REGION: 'Region',
                        CAMPAIGN_PRODUCT_LINE: 'Product Line',
                        CAMPAIGN_MODELS: 'Model',
                        CAMPAIGN_OWNER: 'Owner',
                        CAMPAIGN_CREATE_START: 'Created Time Range',
                        CAMPAIGN_CREATE_END: 'Created Time Range'}                        


campaign_option_default = {CAMPAIGN_ID: 0,
                        CAMPAIGN_REGION: 0,
                        CAMPAIGN_PRODUCT_LINE: 'null',
                        CAMPAIGN_MODELS: 'null',
                        CAMPAIGN_OWNER: 'null', 
                        CAMPAIGN_CREATE_START: 'null', 
                        CAMPAIGN_CREATE_END: 'null'}

#TODO 1: Get the log file
INFLUENCER_SEARCH_OPT_LOG_FILE = r"data/influencer_search_opt_logs.csv"
CAMPAIGN_SEARCH_OPT_LOG_FILE = r"data/campaign_search_opt_logs.csv"
#TODO 2: Parse the content_request


def one_row_inf_search_opt_parser(row_data):
    items = row_data.split('\n')
    items.remove("")
    print(f"one row is: {row_data}")
    a_dict = dict((k.strip(), v.strip())
                  for k, v in (item.split(':', 1) for item in items))
    try:
        page_num = a_dict[PAGE_NUM].strip("[]\"")
        if page_num == '1':
            for key_label in options_count.keys():
                try:
                    if a_dict[key_label].strip("[]\"") != options_default[key_label]:
                        options_count[key_label] += 1
                except KeyError:
                    continue
            return 1
        else:
            return 0
    except KeyError:
        return 0


#TODO 3: Get the non-empty columns
#TODO 4: Count the times of query option

def influencer_search_opt_analyze(data):
    rows = get_log_column(data, 'request_content')
    row_count = 0
    count_1 = 0
    count_non1 = 0
    for record in rows:
        row_count += 1
        if one_row_inf_search_opt_parser(record):
            count_1 += 1
        else:
            count_non1 += 1 

    print(f"Count 1 is {count_1}, Count non 1 is {count_non1}")
    print(options_count)


def one_row_campaign_search_opt_parser(row_data):
    items = row_data.split('\n')
    items.remove("")
    a_dict = dict((k.strip(), v.strip())
                  for k, v in (item.split(':', 1) for item in items))

    for key_label in campaign_option_count.keys():
        try:
            if a_dict[key_label].strip("[]\"") != campaign_option_default[key_label]:
                campaign_option_count[key_label] += 1
        except KeyError:
            continue


def campaign_search_opt_analyze(data):
    rows = get_log_column(data, 'request_content')
    for record in rows:
        one_row_campaign_search_opt_parser(record)
    
    print(campaign_option_count)


def output_influencer_option_search_usage_count(w):
    df = pd.DataFrame({'Options': options_name.values(), 'Counts': options_count.values()})
    df = df.drop([9, 11, 13])  # Remove useless rows
    df = df.sort_values(by=['Counts'], ascending=False)
    df.to_excel(w, sheet_name='InfluencerSearchOptionUsage')


def output_campaign_option_search_usage_count(w):
    df = pd.DataFrame({'Options': campaign_option_name.values(), 'Counts': campaign_option_count.values()})
    df = df.drop([6])  # Remove useless rows
    df = df.sort_values(by=['Counts'], ascending=False)
    df.to_excel(w, sheet_name='CampaignSearchOptionUsage')




logs = pd.read_csv(INFLUENCER_SEARCH_OPT_LOG_FILE)
influencer_search_opt_analyze(logs)

logs = pd.read_csv(CAMPAIGN_SEARCH_OPT_LOG_FILE)
campaign_search_opt_analyze(logs)

with pd.ExcelWriter("output/option_search_usage_report.xlsx") as writer:
    output_influencer_option_search_usage_count(writer)
    output_campaign_option_search_usage_count(writer)
