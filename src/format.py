class Format:
    COLOREND = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    PURPLE = 4
    BOLD = 5
    UNDERLINE = 6

    mapping = {}

    mapping[COLOREND] = "\033[0m"
    mapping[PURPLE] = "\033[34m"
    mapping[RED] = "\033[91m"
    mapping[GREEN] = "\033[92m"
    mapping[YELLOW] = "\033[93m"
    mapping[BOLD] = "\033[1m"
    mapping[UNDERLINE] = "\033[4m"

    def format(input, style):
        if style in range(6):
            output = f"{Format.mapping[style]}{input}{Format.mapping[0]}"
            return output
        else:
            print("Wrong code!")

    def generate_issue_output(
        label,
        issue_color,
        severity,
        likelihood,
        impact,
        exploitability,
        issue_complexity,
        version
    ):
        issue_elements = []

        if likelihood == 0: # special condition 1
            likelihood = 1

        if impact == 0: # special condition 1
            impact = 1

        text_likelihood = (
            Format.format("Likelihood [1-5]: ", Format.BOLD) + f"{likelihood}"
        )

        text_impact = Format.format("Impact [1-5]: ", Format.BOLD) + f"{impact}"

        text_exploitability = (
            Format.format("Exploitability [0-2]: ", Format.BOLD) + f"{exploitability}"
        )

        text_issue_complexity = (
            Format.format("Complexity [0-2]: ", Format.BOLD) + f"{issue_complexity}"
        )

        text_label = (
            Format.format("Final Score: ", Format.BOLD)
            + "{:.1f}".format(severity)
            + f" ({Format.format(label, issue_color)})"
        )

        text_version = (
            Format.format("Hacken Calculator Version: ", Format.BOLD)
            + f"{version}"
        )

        issue_elements.append(text_likelihood)
        issue_elements.append(text_impact)
        issue_elements.append(text_exploitability)
        issue_elements.append(text_issue_complexity)
        issue_elements.append(text_label)
        issue_elements.append(text_version)

        [print(elem) for elem in issue_elements]
