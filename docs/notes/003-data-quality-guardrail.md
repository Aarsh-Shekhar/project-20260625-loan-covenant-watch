# Data Quality Guardrail

Domain: finance

This note records an implementation detail for Loan Covenant Watch. The current operating
threshold is `0.57` and review should happen within `72` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
