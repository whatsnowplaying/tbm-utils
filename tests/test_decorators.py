from tbm_utils import (
	DataReader,
	cast_to_list,
	datareader,
)


@cast_to_list(0)
def cast_func_1(arg0):
	return arg0


@cast_to_list(1)
def cast_func_2(arg0, arg1):
	return arg0, arg1


def test_cast_to_list():
	assert cast_func_1('test') == cast_func_1(['test']) == ['test']
	assert cast_func_2('test', 'test') == cast_func_2('test', ['test']) == ('test', ['test'])


@datareader
def func(data):
	return data


class Class:
	def __init__(self, data):
		self.data_reader = data

	@datareader
	@classmethod
	def build(cls, junk, data):
		return cls(data)


def test_datareader():
	assert isinstance(func(b'test'), DataReader)

	# c = Class.build(b'junk', b'test')
	# print(c.datareader)
	# assert isinstance(c.data_reader, DataReader)

	data_reader = DataReader(b'test')
	assert func(data_reader) == data_reader
