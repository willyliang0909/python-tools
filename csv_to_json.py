import pandas as pd
import json

# CSV 文件的路徑
csv_file_path = "milvus-export-data.csv"
# JSON 文件的輸出路徑
json_file_path = "milvus-export-data.json"

# 使用 Pandas 讀取 CSV
df = pd.read_csv(csv_file_path)

# 將 'metadata' 列的字符串轉換為 JSON 對象
df['metadata'] = df['metadata'].apply(json.loads)

# 將 'vector' 列的字符串轉換為列表
df['vector'] = df['vector'].apply(json.loads)

# 將 DataFrame 轉換為 JSON 格式並保存
df.to_json(json_file_path, orient="records", lines=False, force_ascii=False, indent=4)

print(f"CSV 已成功轉換為 JSON，並保存為 {json_file_path}")
