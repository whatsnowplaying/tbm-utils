import os
from io import DEFAULT_BUFFER_SIZE, BytesIO, FileIO
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from tbm_utils import DataReader

temp_file = NamedTemporaryFile(delete=False)
data_file = Path(temp_file.name)
data_file.write_bytes(b'b' * DEFAULT_BUFFER_SIZE)
data_file_size = os.path.getsize(data_file)


def test_DataReader_BytesIO():
	data = DataReader(
		BytesIO(data_file.read_bytes())
	)

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()


def test_DataReader_DataReader_FileIO():
	data = DataReader(
		DataReader(
			FileIO(data_file, 'rb')
		)
	)

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()


def test_DataReader_DataReader_BytesIO():
	data = DataReader(
		DataReader(
			BytesIO(data_file.read_bytes())
		)
	)

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()


def test_DataReader_FileIO():
	data = DataReader(FileIO(data_file, 'rb'))

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()


def test_DataReader_bytes():
	data = DataReader(data_file.read_bytes())

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()


def test_DataReader_fileobj():
	data = DataReader(data_file.open('rb'))

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()


def test_DataReader_filepath():
	data = DataReader(data_file)

	assert len(data.peek(10)) == 10
	assert len(data.peek()) == DEFAULT_BUFFER_SIZE
	assert len(data.peek(100000)) == DEFAULT_BUFFER_SIZE

	assert data.peek(10) == data.read(10)

	data.seek(-10, os.SEEK_CUR)
	assert data.tell() == 0

	assert len(data.read()) == data.tell() == data_file_size

	data.seek(-10, os.SEEK_END)
	assert data.tell() == data_file_size - 10
	assert len(data.peek(20)) == 10

	data.seek(0)
	assert data.tell() == 0

	data.seek(10, os.SEEK_SET)
	assert data.tell() == 10

	data.close()

	with pytest.raises(ValueError):
		data.read()
