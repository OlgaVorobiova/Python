import pytest
import requests
import dicttoxml
import xmltodict

addresses_url = 'http://164.92.218.36:8080/api/addresses'
auth = ('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')

address = {
    "address": {
        "id_customer": "",
        "id_manufacturer": "",
        "id_supplier": "",
        "id_warehouse": "",
        "id_country": 1,
        "id_state": "",
        "alias": "artem",
        "company": "",
        "lastname": "Vorobiova",
        "firstname": "Olha",
        "vat_number": "",
        "address1": "Illinska street 184",
        "address2": "",
        "postcode": "",
        "city": "Charkiv",
        "other": "",
        "phone": "",
        "phone_mobile": "",
        "dni": ""
    }
}


def test_get_addresses_response_200():
    response = requests.get(addresses_url, auth=auth)

    assert response.status_code == 200


def test_create_address():
    xml = dicttoxml.dicttoxml(
        address, custom_root='prestashop', attr_type=False)

    response = requests.post(addresses_url, data=xml, auth=auth)

    assert response.status_code == 201
    resultAddress = xmltodict.parse(response.content)['prestashop']['address']

    assert resultAddress['lastname'] == address['address']['lastname']
    id = resultAddress['id']

    response = requests.delete(addresses_url + '/' + id, auth=auth)
