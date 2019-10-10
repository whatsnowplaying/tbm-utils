import pytest

from tbm_utils import (
	humanize_bitrate,
	humanize_duration,
	humanize_filesize,
	humanize_sample_rate
)


@pytest.mark.parametrize(
	'bitrate,humanized',
	[
		(0, '0 bps'),
		(1, '1 bps'),
		(100, '100 bps'),
		(1000, '1 Kbps'),
		(1_000_000, '1 Mbps')
	]
)
def test_humanize_bitrate(bitrate, humanized):
	assert humanize_bitrate(bitrate) == humanized


@pytest.mark.parametrize(
	'duration,humanized',
	[
		(0, '00:00'),
		(1, '00:01'),
		(60, '01:00'),
		(3600, '01:00:00')
	]
)
def test_humanize_duration(duration, humanized):
	assert humanize_duration(duration) == humanized


@pytest.mark.parametrize(
	'filesize,precision,humanized',
	[
		(0, 0, '0 B'),
		(1, 0, '1 B'),
		(1024, 0, '1 KiB'),
		(1500, 2, '1.46 KiB'),
		(1_048_576, 0, '1 MiB'),
		(2_048_576, 2, '1.95 MiB'),
		(1_073_741_824, 0, '1 GiB'),
		(2_073_741_824, 2, '1.93 GiB'),
		(1_099_511_627_776, 0, '1 TiB'),
		(2_099_511_627_776, 2, '1.91 TiB')
	]
)
def test_humanize_filesize(filesize, precision, humanized):
	assert humanize_filesize(filesize, precision=precision) == humanized


@pytest.mark.parametrize(
	'sample_rate,humanized',
	[
		(0, '0 Hz'),
		(1, '1 Hz'),
		(1000, '1 KHz'),
		(44100, '44.1 KHz'),
		(48000, '48 KHz'),
		(96000, '96 KHz')
	]
)
def test_humanize_sample_rate(sample_rate, humanized):
	assert humanize_sample_rate(sample_rate) == humanized
