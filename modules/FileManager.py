import pandas as pd
import os

class FileManager:

    def __init__(self, file_path, nrow):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")
        self.file_path = file_path
        self.nrow = nrow
        self.data = self.read_csv()

    def read_csv(self):
        """Read data from a CSV file."""
        try:
            data = pd.read_csv(self.file_path, nrows=self.nrow, encoding="latin-1")
            print(f"✅ Successfully loaded {len(data)} rows from {self.file_path}")
            return data
        except Exception as e:
            print(f"❌ Error reading {self.file_path}: {e}")
            return None
        
    def get_columns(self):
        """Read column names from the CSV file."""
        try:
            # self.columns = [col for col in self.data.columns if "Axis" in col]
            # self.columns = [col for col in self.data.columns if "Trait" not in col and "Time" not in col]
            columns = [col for col in self.data.columns if "Trait" not in col]
            return columns
        except Exception as e:
            print(f"❌ Error reading columns from {self.file_path}: {e}")
            return []
        
    def get_data(self):
        """Return the loaded DataFrame."""
        return self.data