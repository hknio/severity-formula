
# Change Log
All notable changes to this project will be documented in this file.

## [0.5] - 2024-1-26

### Added
- Project version was added to calculator's output to prevent any conflicts.
- **Half-Dependent** field was introduced for `Exploitability` metric.

### Changed
- `Exploitability` coefficient formula was changed. 
- The distribution graph was replaced.

## [0.4.1] - 2024-1-15

### Changed
- Issue classification style was changed. (e.g CRITICAL -> Critical)
- Precision in the final score was truncated to one decimal.

## [0.4] - 2023-12-18

### Added
- Formatting feature was added.

### Changed
- The order of items `Exploitability` and `Issue Complexity` in the **README.md** file has been changed.

### Fixed
- All functions use strict numbers for calculation now.

## [0.3] - 2023-12-14

### Added 
- A new argument was added to the code for faster input entry.

## [0.2] - 2023-11-20

### Added
Two more special conditions were added programmatically to prevent false results:
- The finding **can** be classified as `Low` when the impact metric is **5** and the likelihood metric is **1**.
- The finding **cannot** be classified as `Low` when the impact metric is  **1** and the likelihood metric is **5**.

### Changed
- Severity distribution graph was replaced.

### Fixed
- Taking the square root slightly increased the severity for numbers less than 1. This problem has been fixed.
 
## [0.1] - 2023-11-07
 
### Added
- The `formula.py` script can be executed in two different modes:
    - Calculation mode (no argument)
    - Graph mode (`-g` or `--graph` argument)
 
### Changed
- Coefficients were changed.
    - **Likelihood** coefficient was increased to **0.5** from **0.45**.
    - **Impact** coefficient was increased to **0.5** from **0.45**.
    - **Issue Complexity** coefficient was increased to **0.2** from **0.1**.
    - **Exploitability** upper-bound was decreased from **2.0** to **1.5**.

- The formula was refactored for an edge case scenario in case both **likelihood** and **impact** metrics are set to **1**.

- Severity thresholds were changed.
    - **Low:** `1.7 < score <= 2.5`
    - **Medium:** `2.5 < score <= 3.5`
    - **High:** `3.5 < score <= 4.5`
    - **Critical:** `4.5 > score`

- Number formatting has been changed in order to obtain more precise results during the graphic creation phase.

### Fixed
- The **Issue Complexity** metric now affects the score **negatively**.
 
