from data_quality_check_group import checkForNulls
from data_quality_check_group import checkForMinMax
from data_quality_check_group import checkForValidValues
from data_quality_check_group import checkDuplicateRow

test1 = {
    "testname": "Check for nulls",
    "test": checkForNulls,
    "column": "monthId",
    "table": "dimMonth"
}

test2 = {
    "testname": "Check for min and max",
    "test": checkForMinMax,
    "column": "month",
    "table": "dimMonth",
    "minimum": 1,
    "maximum": 12
}

test3 = {
    "testname": "Check for valid values",
    "test": checkForValidValues,
    "column": "category",
    "table": "customer",
    "valid_values": {'Individual', 'Company'}
}

test4 = {
    "testname": "Check for duplicates",
    "test": checkDuplicateRow,
    "column": "monthId",
    "table": "dimMonth"
}

