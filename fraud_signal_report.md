# Fraud Signal Report

## Objective

The objective of this report is to identify statistically unusual transaction and user behavior that may indicate potential UPI fraud.

## Fraud Signals Identified

### 1. High-Value Transactions — High Severity

- High-value threshold: 9461.76
- High-value transactions: 1477

Transactions above the statistical upper limit were treated as potential high-value anomalies.

### 2. New Accounts Making Large Payments — High Severity

- New accounts making large payments: 1437

New accounts combined with unusually large transaction amounts represent an important risk signal.

### 3. Multiple Device Usage — Medium Severity

- Users with multiple devices: 1332

Multiple-device usage may indicate unusual account behavior and should be monitored along with other fraud indicators.

### 4. Late-Night Transaction Activity — Medium Severity

- Late-night transactions: 10401
- Fraud transactions during late night: 3042
- Late-night fraud percentage: 29.25%

Early-morning transaction activity shows a notable level of fraud and should receive additional monitoring.

### 5. Rapid Transaction Bursts — Medium Severity

- Rapid transaction burst transactions: 733

Frequent or rapid transactions can indicate unusual transaction behavior and should be investigated when combined with other risk signals.

## Severity Ranking

| Rank | Fraud Signal | Severity |
|---|---|---|
| 1 | High-value transactions | High |
| 2 | New accounts making large payments | High |
| 3 | Multiple device usage | Medium |
| 4 | Late-night transaction activity | Medium |
| 5 | Rapid transaction bursts | Medium |

## Recommendations

- Monitor unusually high-value transactions.
- Apply additional checks to new accounts making large payments.
- Monitor repeated device changes.
- Investigate rapid transaction bursts.
- Monitor unusual early-morning activity.
- Combine multiple fraud signals before taking action.

## Conclusion

The analysis indicates that high transaction amounts, new-account activity, multiple-device usage, rapid transaction bursts, and unusual transaction timing can provide useful statistical fraud signals. These indicators should be combined to improve fraud investigation and risk monitoring rather than relying on a single signal.