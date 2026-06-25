# Rule-Based Medical Expert System

A simple Python-based rule engine that demonstrates forward chaining in a medical diagnosis context. The system takes a list of symptoms from the user and infers conclusions using a set of predefined rules.

## Features

- Rule-based inference engine using forward chaining
- Accepts user symptoms as comma-separated input
- Infers medical conditions and recommendations
- Displays the reasoning steps and final conclusions

## How it works

1. The system defines a set of rules where each rule has conditions and a conclusion.
2. User-provided symptoms are collected as initial facts.
3. The forward chaining algorithm repeatedly applies rules whose conditions are satisfied by the current facts.
4. Newly inferred conclusions are added to the facts until no additional rules can fire.
5. The system prints the inference trace, conclusions, and all known facts.

## Usage

1. Open a terminal in the project directory.
2. Run the script with Python:

```bash
python "Expert_System.py"
```

3. Enter symptoms separated by commas when prompted, for example:

```text
fever, cough, headache
```

4. Review the inference steps, final conclusions, and all known facts.

## Example rules included

- `fever + cough => flu`
- `sore_throat + fever => infection`
- `flu + headache => severe_flu`
- `flu + body_ache => viral_illness`
- `severe_flu + fatigue => doctor_visit`
- `viral_illness => rest_and_hydration`

## Requirements

- Python 3.x

## Project Structure

- `Expert System.py` - main application script
- `README.md` - project documentation

## Notes

- This project is intended as a learning demonstration of forward chaining and rule-based reasoning.
- The rule set is simple and does not represent actual medical diagnosis logic.
