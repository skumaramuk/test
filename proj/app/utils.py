typs = {
  "semantic_types": [
    {
      "name": "identity-npi",
      "alias": "NPI",
      "category": "identity",
      "sub_category": null,
      "id": "c3033d7f-5c7b-4433-ad26-78e6415164ba",
      "type": "string"
    },
   {
      "name": "identity-npi",
      "alias": "NPI",
      "category": "identity",
      "sub_category": null,
      "id": "c3033d7f-5c7b-4433-ad26-78e6415164ba",
      "type": "string"
    },
   {
      "name": "identity-npi",
      "alias": "NPI",
      "category": "identity",
      "sub_category": null,
      "id": "c3033d7f-5c7b-4433-ad26-78e6415164ba",
      "type": "string"
    }]
}


def where(main_dict, filter_dict):
    return [x for x in main_dict if all(k in x and x[k] == v for k, v in filter_dict.items())]


def filter_types(**kwargs):
    return where(types['semantic_types'], kwargs)
