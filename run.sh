#!/bin/bash

# Clean Piecewise Linear Reimbursement Calculator
# 
# This implementation uses the decoded business rules:
# - Base daily allowance: $75/day  
# - Mileage rate: $0.48/mile
# - Receipt reimbursement: 31% base rate
# - Logical adjustments for trip length, receipt amounts, and efficiency
#
# Advantages over complex models:
# - Transparent and interpretable business logic
# - Easy to maintain and modify
# - Clear audit trail for every calculation
# - No overfitting to training data
#
# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>

python3 calculate_reimbursement_smart_hybrid.py "$1" "$2" "$3" 