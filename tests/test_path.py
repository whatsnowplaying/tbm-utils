import os
from pathlib import Path

import pytest

from tbm_utils import convert_unix_path


@pytest.mark.skipif(os.name != 'nt', reason="Windows-only test")
@pytest.mark.parametrize(
	'value',
	[
		'/cygdrive/d/Music/test.mp3',
		'/d/Music/test.mp3',
		'D:/Music/test.mp3',
		'D:\\Music\\test.mp3',
		r'D:\Music\test.mp3'
	]
)
def test_convert_unix_path_windows(value):
	assert convert_unix_path(value) == Path('D:/Music/test.mp3')
