# Hotel Budget Module

## Description

This module provides a foundation for budget management in hotels, allowing users to
create and manage budgets for different departments. It includes a base model that
contains common fields for budgets, as well as views that facilitate the visualization
and editing of data.

## Features

- Base Model: 'budget.base', which includes fields for the responsible person,
  description, account number, company, hotel, and months of the year.
- departments Budget: Models that inherits from 'budget.base' and is designed to manage
  budgets for the departments.
- Views: Includes tree, form, and pivot views to facilitate data visualization and
  management.
- Automatic Total Calculation: The total budget is automatically calculated based on the
  values entered for each month.

## Installation

1. Clone the repository.
2. Place the module in the addons directory.
3. Install dependencies
4. Install the module.

## License

AGPL-3

## Creator

Alexandra Suarez Graterol <saya.alex20@gmail.com>
