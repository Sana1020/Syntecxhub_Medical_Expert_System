# Rule-Based Expert System using Forward Chaining

class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = set(conditions)
        self.conclusion = conclusion


def forward_chaining(facts, rules):
    inferred = set(facts)
    inference_log = []

    changed = True

    while changed:
        changed = False

        for rule in rules:
            if (
                rule.conditions.issubset(inferred)
                and rule.conclusion not in inferred
            ):
                inferred.add(rule.conclusion)

                step = (
                    f"{' AND '.join(rule.conditions)} "
                    f"=> {rule.conclusion}"
                )

                inference_log.append(step)
                changed = True

    return inferred, inference_log


def main():
    print("=" * 50)
    print("Medical Expert System")
    print("=" * 50)

    print("\nAvailable Symptoms:")
    print("- fever")
    print("- cough")
    print("- headache")
    print("- sore_throat")
    print("- body_ache")
    print("- fatigue")

    user_input = input(
        "\nEnter symptoms separated by commas: "
    )

    facts = {
        symptom.strip().lower()
        for symptom in user_input.split(",")
        if symptom.strip()
    }

    rules = [
        Rule(
            ["fever", "cough"],
            "flu"
        ),

        Rule(
            ["sore_throat", "fever"],
            "infection"
        ),

        Rule(
            ["flu", "headache"],
            "severe_flu"
        ),

        Rule(
            ["flu", "body_ache"],
            "viral_illness"
        ),

        Rule(
            ["severe_flu", "fatigue"],
            "doctor_visit"
        ),

        Rule(
            ["viral_illness"],
            "rest_and_hydration"
        )
    ]

    final_facts, log = forward_chaining(
        facts,
        rules
    )

    print("\nInference Steps:")
    print("-" * 50)

    if log:
        for step in log:
            print(step)
    else:
        print("No rules were triggered.")

    print("\nConclusions:")
    print("-" * 50)

    conclusions = final_facts - facts

    if conclusions:
        for conclusion in conclusions:
            print(conclusion)
    else:
        print("No conclusion reached.")

    print("\nAll Known Facts:")
    print("-" * 50)

    for fact in sorted(final_facts):
        print(fact)


if __name__ == "__main__":
    main()