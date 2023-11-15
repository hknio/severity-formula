from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import argparse

# v1.1
# Max score: 5, Min score: 0

# if Severity > 4.5, Critical
# if 4.5 >= Severity > 3.4, High
# if 3.4 >= Severity > 2.5, Medium
# if 2.5 >= Severity > 1.7, Low
# if 1.7 >= Severity, Informational


def calculate():
    try:
        # Likelihood bounds between 1-5
        likelihood = int(input("Likelihood [1-5]: "))
        if likelihood not in range(1, 6):
            raise ValueError

        # Impact bounds between 1-5
        impact = int(input("Impact [1-5]: "))
        if impact not in range(1, 6):
            raise ValueError

        # Exploitability bounds between 1-2
        exploitability = int(input("Exploitability [1, 2]: "))
        if exploitability not in range(1, 3):
            raise ValueError

        # IssueComplexity bounds between 0-2
        issue_complexity = int(input("Complexity [0-2]: "))
        if issue_complexity not in range(3):
            raise ValueError

        severity = calculate_severity(
            likelihood, impact, exploitability, issue_complexity
        )

        label = generate_label(severity)

        print(f"Final Score: {severity} ({label})")

    except ValueError:
        print("Value Error!")


def calculate_severity(likelihood, impact, exploitability, issue_complexity):
    exploitability_coeff = 1 + ((exploitability - 1) / exploitability)

    if likelihood == 1:
        likelihood = 0

    if impact == 1:
        impact = 0

    if (likelihood == 0) and (impact == 0):
        result = 0
    else:
        result = ((0.5 * likelihood) + (0.5 * impact) - (0.2 * issue_complexity)) ** (
            1 / exploitability_coeff
        )
    return result


def generate_label(score):
    if float(score) <= 1.7:
        label = "Informational"
    elif 1.7 < float(score) <= 2.5:
        label = "Low"
    elif 2.5 < float(score) <= 3.5:
        label = "Medium"
    elif 3.5 < float(score) <= 4.5:
        label = "High"
    else:
        label = "Critical"
    return label


def generate_dataset():
    count_set = {}
    data = {}

    (
        data["Informational"],
        data["Low"],
        data["Medium"],
        data["High"],
        data["Critical"],
    ) = ({}, {}, {}, {}, {})

    for likelihood in range(1, 6):
        for impact in range(1, 6):
            for exploitability in range(1, 3):
                for complexity in range(3):
                    result = calculate_severity(
                        likelihood, impact, exploitability, complexity
                    )
                    result = "{:.2f}".format(result)

                    if result not in count_set:
                        count_set[result] = 1
                    else:
                        count_set[result] += 1

                    label = generate_label(result)

                    data[label][result] = count_set[result]

    return data


def create_graph(dataset):
    severities, scores, total_count = [], [], []

    for severity in dataset:
        for score in dataset[severity]:
            severities.append(severity)
            scores.append(score)
            total_count.append(dataset[severity][score])

    data = {"Severities": severities, "Score": scores, "Total_count": total_count}

    df = pd.DataFrame(data)
    df = df.sort_values(by=["Score"])

    cols = [
        "#ababab",
        "#49d10f",
        "#ffc800",
        "#e00d09",
        "#5c2670",
    ]

    ax = sns.barplot(
        x="Score",
        y="Total_count",
        data=df,
        hue="Severities",
        dodge=False,
        width=0.8,
        palette=cols,
    )
    plt.title("Sorted severity scores")
    plt.xticks(rotation=90)
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g",
        "--graph",
        help="creates a distribution graph for benchmarking purposes",
        action="store_true",
    )
    args = parser.parse_args()

    if args.graph:
        dataset = generate_dataset()
        create_graph(dataset)
    else:
        calculate()
