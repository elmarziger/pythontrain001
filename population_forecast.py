import argparse
from typing import List


def compute_growth_rates(population: List[float]) -> List[float]:
    """Compute fractional growth rates between consecutive periods."""
    if len(population) < 2:
        return []
    return [population[i] / population[i - 1] - 1 for i in range(1, len(population))]


def forecast_population(population: List[float], years_ahead: int) -> List[float]:
    """Forecast population using average growth rate."""
    rates = compute_growth_rates(population)
    if not rates:
        raise ValueError("Need at least two periods of data to forecast")
    avg_growth = sum(rates) / len(rates)
    current = population[-1]
    forecasts = []
    for _ in range(years_ahead):
        current *= (1 + avg_growth)
        forecasts.append(current)
    return forecasts


def main() -> None:
    parser = argparse.ArgumentParser(description="Forecast future population")
    parser.add_argument("population", nargs="+", type=float, help="Historical population numbers in chronological order")
    parser.add_argument("--years", type=int, default=1, help="Number of future periods to forecast")

    args = parser.parse_args()
    history = args.population
    years = args.years

    try:
        forecasts = forecast_population(history, years)
    except ValueError as e:
        parser.error(str(e))

    for i, value in enumerate(forecasts, 1):
        print(f"Year {i}: {value:.2f}")


if __name__ == "__main__":
    main()
