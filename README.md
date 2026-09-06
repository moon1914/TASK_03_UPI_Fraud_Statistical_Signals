# TASK 03 - UPI Fraud Statistical Signals

## 1. Problem Statement

The objective of this project is to identify statistical signals and suspicious behavioral patterns associated with fraudulent UPI transactions. Statistical analysis and visualization techniques are used to detect unusual transaction amounts, transaction frequency, device changes, account age patterns, and transaction timing.

## 2. Dataset Description

The dataset contains UPI transaction records with 26,393 rows and 65 columns.

Important variables include:
- Transaction amount
- Transaction time of day
- Transaction velocity
- Requester account age
- Receiver account age
- Device information
- Fraud indicator

## 3. Statistical Methods

The following methods were used:

- Descriptive statistics
- IQR method for outlier detection
- Z-score method
- Distribution analysis
- Correlation analysis
- T-Test
- Group-wise comparison

### T-Test Result

T-statistic: -26.57

P-value: 3.76e-132

The null hypothesis was rejected because the p-value is extremely small. Therefore, transaction amount has a statistically significant relationship with fraud occurrence.

## 4. Fraud Signal Findings

The analysis identified the following suspicious signals:

- High-value transactions: 1,477
- Rapid transaction burst transactions: 733
- Users with multiple devices: 1,332
- Late-night transactions: 10,401
- Late-night fraud transactions: 3,042
- New accounts with large payments: 1,437
- IQR transaction amount outliers: 594
- Z-score outliers: 264

The high-value transaction threshold was approximately 9,461.76.

## 5. Visual Analysis

The project includes visualizations such as:

- Transaction amount distribution
- Box plot of transaction amount
- Correlation heatmap
- Transaction amount vs fraud scatter plot
- Fraud percentage by transaction time
- Other statistical visualizations

The analysis shows that fraudulent transactions generally have higher transaction amounts than normal transactions.

## 6. Business Recommendations

1. Monitor unusually high-value transactions.
2. Flag rapid transaction bursts for additional verification.
3. Monitor accounts that frequently change devices.
4. Apply additional checks to new accounts making large payments.
5. Pay special attention to unusual late-night transaction activity.
6. Use multiple statistical signals together instead of relying on a single indicator.
7. Develop a risk-scoring system for suspicious transactions.

## 7. Future Scope

Future improvements can include:

- Machine learning based fraud detection
- Real-time fraud monitoring
- Automated risk scoring
- Advanced behavioral analysis
- Real-time device and transaction tracking
- Integration with fraud alert systems

## Conclusion

Statistical analysis helps identify unusual transaction behavior and important fraud signals. High transaction amounts, rapid transaction activity, device changes, new-account activity, and unusual transaction timing can be useful indicators for fraud monitoring.