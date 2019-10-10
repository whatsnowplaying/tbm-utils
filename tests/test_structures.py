import pytest

from tbm_utils import AttrMapping, LabelList


class AttrMappingMissing(AttrMapping):
	def __missing__(self, key):
		return "missing"


def test_AttrMapping():
	attr_mapping = AttrMapping(key1='value1', key2='value2')
	attr_mapping_from_mapping = AttrMapping.from_mapping(
		{
			'key1': 'value1',
			'key2': 'value2'
		}
	)

	assert attr_mapping == attr_mapping_from_mapping

	assert repr(attr_mapping) == "<AttrMapping ({'key1': 'value1', 'key2': 'value2'})>"
	assert attr_mapping.__repr__(repr_dict={}) == '<AttrMapping ({})>'

	assert list(attr_mapping.items()) == [('key1', 'value1'), ('key2', 'value2')]
	assert list(attr_mapping.keys()) == ['key1', 'key2']
	assert list(attr_mapping.values()) == ['value1', 'value2']

	assert len(attr_mapping) == 2
	assert list(iter(attr_mapping)) == list(iter({'key1': 'value1', 'key2': 'value2'}))

	with pytest.raises(KeyError):
		attr_mapping['test']

	attr_mapping['key3'] = 'value3'
	assert attr_mapping['key3'] == 'value3'

	del attr_mapping['key3']
	assert 'key3' not in attr_mapping

	attr_mapping.key3 = 'value3'
	assert attr_mapping.key3 == 'value3'

	del attr_mapping.key3
	assert not hasattr(attr_mapping, 'key3')

	with pytest.raises(AttributeError):
		attr_mapping.key3

	with pytest.raises(AttributeError):
		del attr_mapping.key3

	attr_mapping_missing = AttrMappingMissing()
	assert attr_mapping_missing['test'] == 'missing'


def test_LabelList():
	list_mixin = LabelList(['item1', 'item2'])

	assert list_mixin.items == ['item1', 'item2']
	assert repr(list_mixin) == '<LabelList (2 items)>'

	list_mixin.item_label = 'test items'
	assert repr(list_mixin) == '<LabelList (2 test items)>'
