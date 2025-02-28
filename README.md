# HW1-BassModel

## Overview
This repository contains an innovation diffusion analysis using the Bass Diffusion Model to estimate adoption trends. The analysis includes historical data, parameter estimation, and forecasting of future adoption.

## Structure
- **data/**: Contains `brazilTV.xlsx`, the dataset used for analysis.
- **img/**: Stores generated plots (`cumulative_ad.png`, `diffusion_pred.png`, `lcd_tv_over_time.png`). 
- **report/**:
  - `report_source.md`: The main write-up in Markdown.
  - `report1.pdf`: Final PDF report.
- **scripts/**:
  - `codes1.ipynb`: Loads TV sales data, fits Bass model parameters, and forecasts adoption.
  - `Helper.ipynb`: Additional notebook with supporting functions.
  - `Helper.py`: Contains reusable functions for Bass model calculations.

 ## Requirements
```` bash
pip install -r requirements.txt
```` 
The project requires the following Python libraries:
numpy
pandas
scipy
matplotlib


## Author
Sona Stepanyan
