Financial Risk Analysis and Portfolio Optimization Toolkit (Python)

This repository contains a set of Python functions designed to process financial data and perform advanced risk analysis. The toolkit automates the workflow from data ingestion to the calculation of key risk metrics.
Key Features:

    Data Ingestion & Preprocessing: * Loads financial data from Excel/CSV files into Pandas DataFrames.

        Automatically converts returns (returns/100) and formats dates (Year-Month index).

    Performance Metrics: * Calculation of Annualized Returns and Volatility.

        Sharpe Ratio computation for risk-adjusted performance analysis.

        Maximum Drawdown tracking.

    Statistical Analysis & Normality Tests:

        Higher-order moments: Skewness and Kurtosis.

        Jarque-Bera Test to assess the normality of return series.

    Risk Management (VaR & CVaR):

        Implementation of Value at Risk (VaR) and Conditional Value at Risk (CVaR/Expected Shortfall).

        Supports three methodologies: Historical, Parametric (Gaussian), and Semi-Parametric (Cornish-Fisher).
        
        Semi-deviation calculation for downside risk analysis.

        Implementation of the efficient frontier plot for two or N assets, using a quadratic optimizer to find the minimum portfolio volatility for a given target return.

