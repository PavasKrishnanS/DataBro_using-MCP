import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import StringIO, BytesIO
from fastmcp import FastMCP
from typing import Dict, Any

# Initialize the FastMCP Server
mcp = FastMCP("DataBro Server")

# Helper Function to Read Data
def read_csv_data(csv_text: str) -> pd.DataFrame:
    """Safely read CSV text into a Pandas DataFrame."""
    try:
        df = pd.read_csv(StringIO(csv_text))
        return df
    except Exception as e:
        raise ValueError(f"Error reading CSV data: {e}")

# CSV Summarizer Tool
@mcp.tool()
def summarize_csv(csv_text: str) -> Dict[str, Any]:
    """
    Analyzes the provided CSV text and returns a comprehensive summary.
    """
    df = read_csv_data(csv_text)
    
    # Generate statistics
    summary = df.describe(include='all').to_string()
    
    # Get column info as string
    buffer = StringIO()
    df.info(buf=buffer)
    col_info = buffer.getvalue()
    
    return {
        "data_shape": f"{df.shape[0]} rows, {df.shape[1]} columns",
        "column_details": col_info.strip(),
        "descriptive_statistics": summary
    }

# Graph/Chart Creation Tool
@mcp.tool()
def create_bar_chart(csv_text: str, column_x: str, column_y: str, title: str) -> str:
    """
    Generates a bar chart from two columns in the CSV data.
    """
    df = read_csv_data(csv_text)
    
    if column_x not in df.columns or column_y not in df.columns:
        return f"Error: Columns '{column_x}' or '{column_y}' not found in data."
    
    # Create the chart
    plt.figure(figsize=(8, 5))
    plt.bar(df[column_x], df[column_y], color='skyblue')
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return f"Base64 Image Data (PNG): {img_base64}"

# Run the Server
if __name__ == "__main__":
    print("Starting FastMCP Data Analysis Server...")
    mcp.run()