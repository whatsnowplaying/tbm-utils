from tbm_utils import (
	AttrMapping,
	convert_default_keys,
	get_defaults,
)


def test_convert_default_keys():
	assert convert_default_keys('item') == 'item'
	assert convert_default_keys(
		{
			'key1': 'value1',
			'--key2': 'value2',
			'--key-3': 'value3',
		}
	) == {
		'key1': 'value1',
		'key2': 'value2',
		'key_3': 'value3',
	}


def test_get_defaults():
	config = {}
	assert get_defaults('command', config) == AttrMapping()

	config['defaults'] = {'option': 'value'}
	assert get_defaults('command', config) == AttrMapping(option='value')

	config['defaults']['command'] = {'option': 'command-value'}
	assert get_defaults('command', config) == AttrMapping(
		command={'option': 'command-value'},
		option='command-value',
	)
	assert get_defaults(
		'comm',
		config,
		command_aliases={'comm': 'command'},
	) == AttrMapping(
		command={'option': 'command-value'},
		option='command-value',
	)

	config['defaults']['comm'] = {'option': 'command-value'}
	assert get_defaults(
		'command',
		config,
		command_keys={'comm'}
	) == AttrMapping(
		command={'option': 'command-value'},
		option='command-value',
	)

	del config['defaults']['command']
	assert get_defaults('comm', config) == AttrMapping(
		comm={'option': 'command-value'},
		option='command-value',
	)
	assert get_defaults(
		'comm',
		config,
		command_aliases={'comm': 'command'},
	) == AttrMapping(
		comm={'option': 'command-value'},
		option='command-value',
	)
