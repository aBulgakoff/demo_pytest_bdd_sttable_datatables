import pytest
from pytest_bdd import scenario, given, then, when, parsers
from sttable import parse_str_table

expected_params = (['https connection', 'http connection', 'ftp connection'],
                   ['http connection', 'https connection', 'ftp connection'])


@pytest.mark.parametrize('parameters', expected_params)
@scenario('data_tables.feature', 'I use datatables')
def test_datatables(datatable, parameters):
    print(f'Print whole datatable container:{datatable}')


@given(parsers.parse('the following users exist:\n{table_with_header}'))
def users_exist(datatable, table_with_header):
    datatable.users = parse_str_table(table_with_header)


@when(parsers.parse('parameters exist:\n{table_no_header}'))
def parameters_exist(datatable, table_no_header, parameters):
    datatable.parameters = parse_str_table(table_no_header, table_with_header=False)
    assert sorted(datatable.parameters.get_column(0)) == sorted(parameters)


@then(parsers.parse('I should see the following names:\n{one_col_table_w_header}'))
def article_is_published(datatable, one_col_table_w_header):
    expected_table = parse_str_table(one_col_table_w_header)

    for field in expected_table.fields:
        assert datatable.users.columns[field] == expected_table.columns[field]
