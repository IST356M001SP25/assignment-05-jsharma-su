from datetime import datetime
import re

def clean_currency(item: str) -> float:
    '''
    Remove anything from the item that prevents it from being converted to a float
    '''
    if not item:
        return 0.0
    cleaned = re.sub(r'[\d.-]', '', item) #removes anything that is not a digit, . or -
    return float(cleaned) if cleaned else 0.0

def extract_year_mdy(timestamp: str) -> int:
    '''
    Use the datetime.strptime to parse the date and then extract the year
    '''
    try:
        date_obj = datetime.strptime(timestamp, '%m/%d/%Y')
        return date_obj.year
    except ValueError:
        return None # or raise an error if preferred

def clean_country_usa(item: str) -> str:
    '''
    This function should replace any combination of 'United States of America', 'USA' etc. with 'United States'
    '''
    possibilities = [
        'united states of america', 'usa', 'us', 'united states', 'u.s.'
    ]
    item_lower = item.strip().lower()
    if item_lower in possibilities:
        return 'United States'
    return item.strip().title()

if __name__ =='__main__':
    print(clean_currency("1,234.56"))       #1234.56
    print(clean_currency("USD 500"))        #500.0
    print(clean_currency(""))               # 0.0

    print(extract_year_mdy("12/25/2020"))   #2020
    print(extract_year_mdy("01/01/1999"))   #1999

    print(clean_country_usa("USA"))         #United States
    print(clean_country_usa("United States"))   #United States
    print(clean_country_usa("India"))       #India