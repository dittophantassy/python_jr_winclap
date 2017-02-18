import csv
from operator import itemgetter


def get_campaigns(filename):
    # id,payout,impressions,installs
    with open(filename) as csvfile:
        return list(csv.DictReader(csvfile))


def get_formatted_campaigns(filename):
    campaigns = get_campaigns(filename)
    formatted_campaigns = []
    for campaign in campaigns:
        formatted_campaigns.append({
            'id': int(campaign['id']),
            'payout': float(str(campaign['payout']).replace(',', '.')),
            'impressions': int(campaign['impressions']),
            'installs': int(campaign['installs'])
        })
    return formatted_campaigns


def order_by_payout(filename):
    """
    Returns a list of campaigns ID's, order by payout from highest to lowest.
    """
    campaigns = get_formatted_campaigns(filename)

    return [d['id'] for d in sorted(campaigns,  # the id as integer
                                    # from the list ordered by payout
                                    key=itemgetter('payout'),
                                    reverse=True)]  # from largest to smallest


def order_by_total_payout(filename):
    """
    Returns a list of campaigns ID's, order by total payout from highest to
    lowest.
    >>> total_payout = payout * installs
    """
    campaigns = get_formatted_campaigns(filename)

    return [d['id'] for d in sorted(campaigns,  # the id as integer
                                    # by the payout * installs
                                    key=lambda d: d['payout'] * d['installs'],
                                    reverse=True)]  # from largest to smallest


def order_by_cr(filename):
    """
    Returns a list of campaigns ID's, order by conversion rate (CR) from highest
    to lowest.
    >>> cr = impressions / installs
    """
    campaigns = get_formatted_campaigns(filename)
    return [d['id'] for d in sorted(campaigns,  # the id as integer
                                    # by impressions / installs
                                    key=lambda d: d[
                                        'impressions'] / d['installs'],
                                    reverse=False)]  # from largest to smallest


if __name__ == '__main__':
    payout_order = [17, 14, 22, 7, 11, 15, 23, 13, 18, 12, 6, 1, 3, 10, 25, 24,
                    21, 16, 20, 5, 4, 8, 9, 19, 2]
    total_payout_order = [15, 11, 18, 7, 14, 21, 3, 6, 25, 13, 16, 5, 24, 20,
                          17, 23, 1, 10, 8, 9, 19, 12, 4, 22, 2]
    cr_order = [11, 15, 18, 25, 21, 7, 8, 24, 6, 14, 3, 9, 5, 16, 19, 10, 20,
                2, 13, 4, 17, 1, 23, 12, 22]
    assert order_by_payout('campaigns.csv') == payout_order
    assert order_by_total_payout('campaigns.csv') == total_payout_order
    assert order_by_cr('campaigns.csv') == cr_order
