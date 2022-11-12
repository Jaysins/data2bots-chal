from pprint import pprint
import json

value_store = {"str": "string", "int": "integer"}

advanced_value_type = [dict, list]


def decode_array(arr):
    """

    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    if not arr:
        return "enum"
    return "enum" if type(arr[0]) == str else "array"


def read_data_type(data_value):
    value_type = type(data_value).__name__
    value_result = value_store.get(str(value_type))
    if value_result:
        return value_result
    if value_type == "list":
        return decode_array(data_value)
    if value_type == "dict":
        return sniff(data_value)
    return "unknown"


def sniff(data):
    """

    :param data:
    :type data:
    :return:
    :rtype:
    """
    result = dict()
    for key, value in data.items():
        resulted_value = read_data_type(value)
        result[key] = resulted_value if type(resulted_value) in advanced_value_type else dict(type=resulted_value,
                                                                                              tag="", description="",
                                                                                              required=False)
    return result
