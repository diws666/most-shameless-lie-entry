import os

# Verified count: 75 characters (75 bytes UTF-8).
LINE = "The most shameless lie I ever told: 'I have read the terms and conditions.'"

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)
