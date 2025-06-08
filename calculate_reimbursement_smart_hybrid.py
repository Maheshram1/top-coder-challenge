#!/usr/bin/env python3

import sys
import math
from calculate_reimbursement_segmented_fixed import calculate_reimbursement as segmented_model

def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    """
    Smart hybrid: Use interview insights to choose the best approach for each case
    """
    days = int(trip_duration_days)
    miles = float(miles_traveled)
    receipts = float(total_receipts_amount)
    
    efficiency = miles / days if days > 0 else 0
    daily_receipts = receipts / days if days > 0 else 0
    
    # Get segmented model prediction as base
    base_prediction = segmented_model(days, miles, receipts)
    
    # Apply SELECTIVE adjustments based on interview insights
    
    # 1. Efficiency sweet spot bonus (only for mid-range efficiency)
    if 180 <= efficiency <= 220 and days >= 3 and receipts > 100:
        # Small bonus for efficient trips
        base_prediction += min(15.0, 0.05 * miles)
    
    # 2. Over-efficiency penalty (only for extreme cases)
    elif efficiency > 400 and receipts < 500:
        # Penalize suspiciously fast trips with low receipts
        base_prediction -= min(20.0, 0.02 * miles)
    
    # 3. Small receipt penalty (only for longer trips)
    if receipts < 50 and days >= 4:
        # Penalty for suspiciously low receipts on long trips
        penalty = min(25.0, (50 - receipts) * 0.3)
        base_prediction -= penalty
    
    # 4. 5-day special case (small adjustment)
    if days == 5 and 100 <= efficiency <= 250:
        # Small bonus for typical 5-day business trips
        base_prediction += 8.0
    
    # 5. Rounding adjustment for .49/.99 cases
    fractional_part = base_prediction - int(base_prediction)
    if 0.48 <= fractional_part <= 0.50 or 0.98 <= fractional_part <= 1.00:
        base_prediction += 0.01

    return round(base_prediction, 2)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 calculate_reimbursement_smart_hybrid.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        sys.exit(1)
    
    try:
        days = sys.argv[1]
        miles = sys.argv[2]
        receipts = sys.argv[3]
        
        result = calculate_reimbursement(days, miles, receipts)
        print(result)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1) 