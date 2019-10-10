from tbm_utils import cast_to_list


@cast_to_list(0)
def cast_func_1(arg0):
	return arg0


@cast_to_list(1)
def cast_func_2(arg0, arg1):
	return arg0, arg1


def test_cast_to_list():
	assert cast_func_1('test') == cast_func_1(['test']) == ['test']
	assert cast_func_2('test', 'test') == cast_func_2('test', ['test']) == ('test', ['test'])
