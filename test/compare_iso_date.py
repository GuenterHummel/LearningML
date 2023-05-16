from datetime import datetime

_EXTRACTOR_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S,%f'
_DB_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S,%f'


def sanitize_datetime(datetime_value: str | int) -> str:
    if datetime_value == 0:
        return "0"

    is_extractor_datetime_format = datetime_value.find(' ') != -1

    if is_extractor_datetime_format:
        date_obj = datetime.strptime(datetime_value, _EXTRACTOR_DATETIME_FORMAT)
        date_obj = date_obj.replace(tzinfo=datetime.utcnow().astimezone().tzinfo)
        return date_obj.isoformat(timespec='milliseconds')

    return datetime_value


def conv_db_datetime_str_to_datetime_obj(datetime_value: str | int) -> datetime:
    if datetime_value == 0:
        return datetime.min

    return datetime.fromisoformat(datetime_value)

def conv_datetime_obj_to_db_datetime_str(datetime_obj: datetime) -> str:
    if datetime_obj == datetime.min:
        return "0"

    return datetime_obj.isoformat(timespec='milliseconds')


testdate_1 = '2023-03-31T22:41:26.000+02:00'
testdate_2 = '2023-03-31T22:41:26.333+02:00'
testdate_3 = 0
testdate_4 = '2023-03-31T22:41:26.444+03:00'
testdate_5 = '2023-03-31T22:41:26.444+02:00'

testdate_1_obj = parse_db_datetime(testdate_1)
testdate_2_obj = parse_db_datetime(testdate_2)
testdate_3_obj = parse_db_datetime(testdate_3)
testdate_4_obj = parse_db_datetime(testdate_4)
testdate_5_obj = parse_db_datetime(testdate_5)

print ("testdate_1 < testdate_2:  " + str(testdate_1 < testdate_2))
print ("testdate_1_obj < testdate_2_obj:  " + str(testdate_1_obj < testdate_2_obj))

print ("testdate_2 < testdate_4:  " + str(testdate_2 < testdate_4))
print ("testdate_2_obj < testdate_4_obj:  " + str(testdate_2_obj < testdate_4_obj))

print ("testdate_4 < testdate_5:  " + str(testdate_4 < testdate_5))
print ("testdate_5_obj < testdate_5_obj:  " + str(testdate_4_obj < testdate_5_obj))
