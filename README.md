
# Climate Change in China: A Decade of Warming? (2011–2020)

> *“History is not the past but a map of the past drawn from a particular point of view to be useful to the modern traveler.”*  
> — Henry Glassie

## Project Overview

This project is submitted for AAE 718 at the University of Wisconsin–Madison. It investigates the average air temperature trend in China over the period 2011 to 2020, based on empirical data from NOAA's Integrated Surface Dataset – Lite (ISD-Lite).

The central inquiry is simple: **Has China warmed over the past decade?**  
The response is drawn from over 10 million hourly observations across hundreds of weather stations.

## Repository Structure

```
.
├── images/
│   └── china_avg_temp_trend_2011_2020_resized.png
├── report.md
├── .gitignore
└── README.md
```

## Data

- **Source**: NOAA ISD-Lite Archive  
- **Scope**: All available Chinese weather stations  
- **Years Covered**: 2011–2020  
- **Metric**: Hourly air temperature, aggregated annually  

Due to size, raw `.zip` or `.tar.gz` data files are not included here. Users may download data for reproduction from:  
🔗 [NOAA ISD-Lite Archive](https://www.ncei.noaa.gov/data/global-summary-of-the-day/archive/)

## How to Reproduce

1. Download the annual ISD-Lite datasets from NOAA for 2011–2020.
2. Extract all `.txt` or `.op` files for Chinese stations into a `data/` folder.
3. Run the processing script (to be added).
4. Output figures will be saved to `/images/`.

All analysis is performed in Python using `pandas`, `matplotlib`, and `weasyprint`.

## Report PDF

📄 [Click here to view the full report](./aae718_china_temp_report_full.pdf)

## License

This project is for academic use only. Feel free to reuse with attribution.  
Forks welcome. Citations preferred. Distortion discouraged.

---
