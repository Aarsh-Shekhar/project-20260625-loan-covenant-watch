# Field Validation

Domain: finance

This note records an implementation detail for Loan Covenant Watch. The current operating
threshold is `0.58` and review should happen within `8` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
