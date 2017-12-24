from flask import jsonify

def comparer(data):
    contract_monthly_total = data['phone_contract']['monthly'] * 24
    contract_total = contract_monthly_total + data['phone_contract']['upfront']

    sim_monthly_total = data['sim_contract']['monthly'] * 24
    sim_total = sim_monthly_total + data['sim_contract']['handset_cost']

    return jsonify({
        'network': data['network'],
        'post_code': data['post_code'],
        'phone_contract': {
            'contract_total': contract_total
        },
        'sim_contract': {
            'sim_total': sim_total
        },
    })
