from pathlib import Path

# import pendulum

from tbm_utils import get_filepaths


TEST_DIR = Path(__file__).parent / 'files'
TEST_FILEPATHS = list(TEST_DIR.iterdir())

# Y2000 = pendulum.period(
# 	pendulum.datetime(2000, 1, 1).start_of('day'),
# 	pendulum.datetime(2000, 12, 31).end_of('day')
# )
# Y2019 = pendulum.period(
# 	pendulum.datetime(2019, 1, 1).start_of('day'),
# 	pendulum.datetime(2019, 12, 31).end_of('day')
# )
# Y2019AUG = pendulum.period(
# 	pendulum.datetime(2019, 8, 1).start_of('day'),
# 	pendulum.datetime(2019, 8, 31).end_of('day')
# )


# TODO: More test situations.
# TODO: Need to figure a workaround or mock for this.
# def test_filter_filepaths_by_dates():
# 	assert list(filter_filepaths_by_dates(TEST_FILEPATHS)) == TEST_FILEPATHS
# 	assert list(
# 		filter_filepaths_by_dates(
# 			TEST_FILEPATHS,
# 			created_in=Y2000
# 		)
# 	) == [TEST_DIR / 'test_file.1']
# 	assert list(
# 		filter_filepaths_by_dates(
# 			TEST_FILEPATHS,
# 			modified_in=Y2000
# 		)
# 	) == [TEST_DIR / 'test_file.1']
# 	assert list(
# 		filter_filepaths_by_dates(
# 			TEST_FILEPATHS,
# 			created_in=Y2019
# 		)
# 	) == TEST_FILEPATHS[1:]
# 	assert list(
# 		filter_filepaths_by_dates(
# 			TEST_FILEPATHS,
# 			modified_in=Y2019
# 		)
# 	) == TEST_FILEPATHS[1:]
# 	assert list(
# 		filter_filepaths_by_dates(
# 			TEST_FILEPATHS,
# 			created_in=Y2019AUG
# 		)
# 	) == TEST_FILEPATHS[1:]
# 	assert list(
# 		filter_filepaths_by_dates(
# 			TEST_FILEPATHS,
# 			modified_in=Y2019AUG
# 		)
# 	) == TEST_FILEPATHS[1:]


def test_get_filepaths():
	assert list(get_filepaths(TEST_FILEPATHS)) == TEST_FILEPATHS
	assert list(get_filepaths([TEST_DIR])) == TEST_FILEPATHS
	assert list(get_filepaths([str(TEST_DIR)])) == TEST_FILEPATHS
	assert list(get_filepaths(TEST_DIR / 'test_file.1')) == [TEST_DIR / 'test_file.1']

	assert list(get_filepaths(TEST_FILEPATHS, exclude_paths=['test_file'])) == []
	assert list(get_filepaths(TEST_FILEPATHS, exclude_regexes=['test_.*'])) == []
	assert list(get_filepaths(TEST_DIR, exclude_paths=['test_file'])) == []
	assert list(get_filepaths(TEST_DIR, exclude_regexes=['test_.*'])) == []
	assert list(get_filepaths(TEST_DIR, exclude_globs=['test_*.*'])) == []
