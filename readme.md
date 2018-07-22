# Contract Comparison API

This is an API implementation of the [ContractCalculus](https://github.com/JHarrowell/ContractCalculus) project that I made whilst working for Three. It allows the user to calculate the difference in price between buying the phone yourself or getting a contract.

## Installation

You'll need Python3

Clone the repo

`git clone git@github.com:JHarrowell/contract-comparison.git` 

CD into the directory 

`cd contract-comparison`

Install the dependencies (I'd recommend using virtualenv or pyenv to keep your envs seperate)

`pip3 install -r requirements.txt`

Run the program

`python3 app.py`

### Usage

More features are planned, check below for a mini-roadmap

`POST /compare`

Example input, there's currently no error checking so anything that deviates from this may break!

```JSON
{
  "network": "EE",
  "currency": "£",
  "device": {
    "model": "Samsung S9",
    "capacity": 64
  },
  "phone_contract": {
    "length": 24,
    "monthly": 43.00,
    "upfront": 50.00
  },
  "sim_contract": {
    "handset_cost": 702.00,
    "monthly": 22.00
  }
}
```

Example output

```JSON
{
  "network": "EE",
  "difference_outcome": "The Samsung S9 on contract is cheaper by £148.0",
  "device": {
    "model": "Samsung S9",
    "capacity": 64
  },
  "phone_contract": {
    "contract_total": 1082,
    "contract_length": 24
  },
  "sim_contract": {
    "sim_total": 1230,
    "contract_length": 24
  }
}
```

#### Roadmap

I'll be adding features as an when I get time, I'm just about to enter my final year of university so time may be scarce, feel free to open pull requests.

• Ability to describe tariffs

• Let you save and retrieve comparisons

Example - `GET /comparison/ee-4gb-s9`

• Compare multiple options at one time

• Factor in insurance costs

• Add a fancy UI




