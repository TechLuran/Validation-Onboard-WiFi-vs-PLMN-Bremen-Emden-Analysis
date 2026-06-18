import os
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

clean_folder = 'data/clean'
csv_files = glob(os.path.join(clean_folder, '*.csv'))

for file_path in csv_files:
    file_name = os.path.basename(file_path)
    df = pd.read_csv(file_path)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    has_rssi = 'rssi_dbm' in df.columns and not df['rssi_dbm'].dropna().empty
    
    if has_rssi:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    else:
        fig, ax1 = plt.subplots(1, 1, figsize=(12, 5))
        ax2 = None
        
    ax1.plot(df['timestamp'], df['rtt_ms'], color='#1f77b4', alpha=0.7, label='RTT (ms)')
    ax1.set_ylabel('RTT (ms)', color='#1f77b4')
    ax1.tick_params(axis='y', labelcolor='#1f77b4')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_title(f"Network Metrics Timeline - {file_name}")
    
    if has_rssi and ax2:
        ax2.plot(df['timestamp'], df['rssi_dbm'], color='#d62728', alpha=0.7, label='RSSI (dBm)')
        ax2.set_ylabel('RSSI (dBm)', color='#d62728')
        ax2.tick_params(axis='y', labelcolor='#d62728')
        ax2.grid(True, linestyle='--', alpha=0.5)
        ax2.set_xlabel('Local Time (Germany)')
    else:
        ax1.set_xlabel('Local Time (Germany)')
        
    plt.tight_layout()
    plot_output_name = file_path.replace('.csv', '_metrics_plot.png')
    plt.savefig(plot_output_name, dpi=300)
    plt.close()