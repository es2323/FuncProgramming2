import csv
from functools import reduce

# ======================
# 1. Pure Data Loading
# ======================
def load_csv(filepath):
    """Pure function: Loads CSV without side effects"""
    with open(filepath, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

# ======================
# 2. FP Data Processing
# ======================
def filter_data(data, substation, date):
    """Pure filter operation"""
    return list(filter(
        lambda row: (row['Substation'] == substation and row['t_date'] == date),
        data
    ))

def calculate_voltage_avg(filtered):
    """FP voltage calculation"""
    voltages = map(
        lambda row: (float(row['V_MIN_Filtered']) + float(row['V_MAX_Filtered'])) / 2,
        filtered
    )
    return reduce(lambda x, y: x + y, voltages) / len(filtered) if filtered else 0

def calculate_current_avg(filtered):
    """FP current calculation"""
    currents = map(
        lambda row: (float(row['I_GEN_MIN_Filtered']) + float(row['I_GEN_MAX_Filtered'])) / 2,
        filtered
    )
    return reduce(lambda x, y: x + y, currents) / len(filtered) if filtered else 0

def calculate_total_power(filtered):
    """FP power summation"""
    powers = map(lambda row: float(row['P_GEN_MIN']), filtered)
    return reduce(lambda x, y: x + y, powers, 0)  # 0 as initial value

# ======================
# 3. Main Pipeline
# ======================
def process_pv_data(filepath, substation, date):
    """Pure function composition"""
    data = load_csv(filepath)
    filtered = filter_data(data, substation, date)
    
    return {
        'substation': substation,
        'date': date,
        'avg_voltage': calculate_voltage_avg(filtered),
        'avg_current': calculate_current_avg(filtered),
        'total_power': calculate_total_power(filtered),
        'record_count': len(filtered)
    }

# ======================
# 4. Execution
# ======================
if __name__ == "__main__":
    result = process_pv_data(
        filepath=r"C:\Users\enosh\Downloads\EXPORT HourlyData - Customer Endpoints.csv",
        substation="Alverston Close",              # Example from dataset
        date="2014-01-07"              # Example date
    )
    
    print(f"""
    PV Data Analysis Report
    --------------------------
    Substation: {result['substation']}
    Date: {result['date']}
    Average Voltage: {result['avg_voltage']:.2f} V
    Average Current: {result['avg_current']:.2f} A
    Total Power Generated: {result['total_power']:.2f} kW
    Records Processed: {result['record_count']}
    """)