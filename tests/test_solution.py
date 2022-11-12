from solution import sniff, read_data_type, decode_array


def test_sniff():
    assert type(sniff(data={"battle": {"id": "123"}})) == dict


def test_read_data_type():
    """

    :return:
    :rtype:
    """
    assert type(read_data_type("1223")) == str


def test_decode_array():
    assert decode_array([]) == "enum"
