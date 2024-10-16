import configuration
import requests
import data


def post_products_kits(product_ids):



    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                              headers=data.headers)


