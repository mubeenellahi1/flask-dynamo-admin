from decimal import Decimal

def remove_empty_fields(dic):
    for key in list(dic.keys()):
        if dic[key] == "":
            del dic[key]
    return dic



def extract_valueset(data):
    parts = []
    valueset={}
    for item in data:
        if 'parts' in item:
            split_item = item.split("].")
            key=split_item[1]
            index = int(split_item[0][-1:])
            if len(parts) <= int(index):
                parts.append({})
            parts[index][key] = data.get(item)
    
    for part in parts:
        part["default"]= {
            "integrity": part["integrity"],
            "confidentiality": part["confidentiality"],
            "availability": part["availability"],
        }
        del part["integrity"]
        del part["confidentiality"]
        del part["availability"]

    valueset["key"] = data.get("key")
    valueset["label"] = data.get("label")
    valueset["level"] = data.get("level")
    valueset["type"] = data.get("type")
    valueset["id"] = "VS"+str(data.get("id"))
    valueset['parts'] = parts
    
    return valueset


def extract_control_family(data):
    control_family={
        "key": data.get("key"),
        "label":data.get("label"),
        "level":data.get("level"),
        "type":data.get("type"),
        "id":"CF"+str(data.get("id")),
        'order':data.get("order"),
    }
    return control_family


def extract_threat(data):
    threat={
        "key": data.get("key"),
        "label":data.get("label"),
        "level":data.get("level"),
        "type":data.get("type"),
        "group":data.get("group"),
        "id":"THR"+str(data.get("id")),
        'default':data.get("default"),
        'description':data.get("description"),
        'parts':{
            "integrity":float(data.get("integrity")),
            "confidentiality":float(data.get("confidentiality")),
            "availability":float(data.get("availability")),
        }
    }
    return threat


def extract_settings(data):
    settings={
        "class":"settings",
        "key": data.get("key"),
        "label":data.get("label"),
        "level":data.get("level"),
        "type":data.get("type"),
        "id":"SET"+str(data.get("id")),
        "group":data.get("group"),
        'group_label':data.get("group_label"),
        "default":data.get("default"),
    }

    settings = remove_empty_fields(settings)
    parts = []

    for item in data:
        if 'parts' in item:
            split_item = item.split("].")
            key=split_item[1]
            index = int(split_item[0][-1:])
            if len(parts) <= int(index):
                parts.append({})

            if data.get(item) == "":
                continue
            elif key == "default":
                parts[index][key] = (data.get(item) == "true")
            else:
                parts[index][key] = data.get(item)
    
    settings['parts'] = parts
    return settings


def extract_control(data):
    control={
        "label":data.get("control_label"),
        "id":data.get("family")+"-"+str(data.get("id")),
    }

    parts = {}
    id = data.get("family")+"-"+str(data.get("id"))

    for item in data:
        value = data.get(item)

        if value== "":
            continue

        if 'control_parts' in item:
            if "depends_on" in item:
                value =  id+"-"+value              


            split_item = item.split('.')
            index = int(split_item[0].replace("control_parts","").replace("[","").replace("]","")) + 1
            key = id+"-"+str(index)
            if key not in parts:
                parts[key] = {"parts": {}}

            if len(split_item) > 2:
                subindex =  split_item[1].replace("parts","").replace("[","").replace("]","")
                parts_key = split_item[2]
                charsubindex = chr(97+int(subindex))
                sub_key = key+'-'+str(charsubindex)
                if sub_key not in parts[key]['parts']:
                    parts[key]['parts'][sub_key] = {}
                
                parts[key]['parts'][sub_key][parts_key] = value

            else:
                parts_key = split_item[1]
                parts[key][parts_key] = value
    
    
    control['parts'] = parts
    return control


def extract_vulnerability(data,threats):
    vulnerability={
        "id":data.get("family")+"-"+str(data.get("id")),
        "default": data.get("vulnerability_default"),
        "label":data.get("vulnerability_label"),
        "level":data.get("vulnerability_level"),
        "type":data.get("vulnerability_type"),
    }

    id = data.get("family")+"-"+str(data.get("id"))

    parts = {}
    relevant_threats = []

    for item in data:
        value = data.get(item)

        if value== "":
            continue

        if "protection_factor" in item:
            value=Decimal(value)

        if 'relevant_threats' in item:
            split_item = item.split("].")
            index = int(item.split("[")[1].replace("]",""))
            relevant_threats.append(threats[index])

        if 'vulnerability_parts' in item:
            split_item = item.split('.')
            index = int(split_item[0].replace("vulnerability_parts","").replace("[","").replace("]","")) + 1
            key = id+"-"+str(index)
            if key not in parts:
                parts[key] = {"parts": {}}

            if len(split_item) > 2:
                subindex =  split_item[1].replace("parts","").replace("[","").replace("]","")
                parts_key = split_item[2]
                charsubindex = chr(97+int(subindex))
                sub_key = key+'-'+str(charsubindex)
                if sub_key not in parts[key]['parts']:
                    parts[key]['parts'][sub_key] = {}    
                
                parts[key]['parts'][sub_key][parts_key] = value

            else:
                parts_key = split_item[1]
                parts[key][parts_key] = value

    
    vulnerability['parts'] = parts
    vulnerability['relevant_threats'] = relevant_threats
    return vulnerability