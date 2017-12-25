from string import Template
from flask import jsonify


def comparer(data):
    sim_cheaper = Template('The $model on sim only is cheaper by $difference.')
    price_equal = Template('The $model costs the same on contract or sim only.')
    contract_cheaper = Template('The $model on contract is cheaper by $difference.')

    contract_monthly_total = data['phone_contract']['monthly'] * data['phone_contract']['length']
    contract_total = contract_monthly_total + data['phone_contract']['upfront']

    sim_monthly_total = data['sim_contract']['monthly'] * data['phone_contract']['length']
    sim_total = sim_monthly_total + data['sim_contract']['handset_cost']

    if contract_total < sim_total:
        difference_amount = sim_total - contract_total
        difference_outcome = contract_cheaper.substitute(model=data['device']['model'], difference=difference_amount)
    elif contract_total == sim_total:
        difference_outcome = price_equal.substitute(model=data['device']['model'])
    else:
        difference_amount = contract_total - sim_total
        difference_outcome = sim_cheaper.substitute(model=data['device']['model'], difference=difference_amount)

    return jsonify({
        'network': data['network'],
        'difference_outcome': difference_outcome,
        'device': {
            'model': data['device']['model'],
            'capacity': data['device']['capacity'],
        },
        'phone_contract': {
            'contract_total': contract_total
        },
        'sim_contract': {
            'sim_total': sim_total
        },
    })
