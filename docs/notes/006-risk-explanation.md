# Risk Explanation

Domain: finance

This note records an implementation detail for Loan Covenant Watch. The current operating
threshold is `0.62` and review should happen within `4` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
