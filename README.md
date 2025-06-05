# Population Forecast Tool

This repository contains a simple Python script for forecasting future population based on historical data.

## Usage

Provide the historical population numbers in chronological order followed by the number of years you want to forecast.

```bash
python3 population_forecast.py 1000 1050 1100 --years 2
```

Output:

```
Year 1: 1153.69
Year 2: 1210.00
```

The script calculates the average growth rate from the historical data and applies it to predict future values.
