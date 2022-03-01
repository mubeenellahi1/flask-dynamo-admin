from boto3.dynamodb.conditions import Key, Attr


def get_metadata(meta_table):
    item_list = meta_table.scan()
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_settings_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('settings'),
                                 FilterExpression=Attr('level').eq('project'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_project_scope_settings_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('project_scope'),
                                 FilterExpression=Attr('level').eq('project'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_control_families_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('control_family'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_control_family_metadata(meta_table, family_code):
    item = meta_table.get_item(Key={'class': 'control_family', 'id': family_code})
    if item and 'Item' in item:
        return item['Item']
    return None


def get_valuesets_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('valueset'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_threats_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('threat'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_vulnerabilities_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('vulnerability'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


def get_controls_metadata(meta_table):
    item_list = meta_table.query(KeyConditionExpression=Key('class').eq('control'))
    if item_list and 'Items' in item_list and len(item_list['Items']) > 0:
        return item_list['Items']
    return []


