from boto3.dynamodb.conditions import Key, Attr



def ddb_create_control(metatable,control):
    control = {
        'class': 'control',
        'label': control['label'],
        'id': control['id'],
        'parts': control['parts']
    }
    result = metatable.put_item(Item=control)
    if result:
        return True
    return result


def ddb_create_vulnerability(metatable,vulnerability):
    vulnerability = {
        'class': 'vulnerability',
        'label': vulnerability['label'],
        'level': vulnerability['level'],
        'relevant_threats': vulnerability['relevant_threats'],
        'id': vulnerability['id'],
        'parts': vulnerability['parts']
    }
    result = metatable.put_item(Item=vulnerability)
    if result:
        return True
    return result


def ddb_create_valueset(metatable,valueset):
    vs = {
        'class': 'valueset',
        'label': valueset['label'],
        'level': valueset['level'],
        'id': valueset['id'],
        'type':valueset['type'],
        'key': valueset['key'],
        'parts': valueset['parts']
    }
    result = metatable.put_item(Item=vs)
    if result:
        return True
    return result


def ddb_create_control_family(metatable,cf):
    cf = {
        'class': 'control_family',
        'label': cf['label'],
        'level': cf['level'],
        'id': cf['id'],
        'type':cf['type'],
        'key': cf['key'],
        'order': str(cf['order'])
    }
    result = metatable.put_item(Item=cf)
    if result:
        return True
    return result


def ddb_create_threat(metatable,threat):
    threat = {
        'class': 'threat',
        'label': threat['label'],
        'level': threat['level'],
        'id': threat['id'],
        'type':threat['type'],
        'key': threat['key'],
        'group': threat['group'],
        'description': threat['description'],
        'default': threat['default'],
        'parts': threat['parts']
    }
    result = metatable.put_item(Item=threat)
    if result:
        return True
    return result


def ddb_create(metatable,item):
    result = metatable.put_item(Item=item)
    if result:
        return True
    return result

