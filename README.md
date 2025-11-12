# 💻 DataBro: Sales Data Analysis & Visualization Server (FastMCP) 📈

This repository hosts a data analysis server built with the **FastMCP** framework. It is designed to process and visualize sales transaction data, specifically developed for use within environments supporting the **Model Context Protocol (MCP)**, such as Claude's desktop application.

It exposes powerful, easy-to-use tools for summarizing CSV datasets and generating visual insights.

https://claude.ai/public/artifacts/1602c219-c9c3-4bca-9311-982147ad74b2?fullscreen=false
---

## 🌟 Features

* **CSV Data Ingestion:** Safely reads and processes sales data from a raw CSV text format using Pandas.
* **Data Summarization:** Provides comprehensive statistical summaries (`df.describe`) and structural column information (`df.info`).
* **Bar Chart Visualization:** Generates and returns Base64 encoded PNG images for quick visual analysis of key metrics (e.g., product performance, sales representative output).
* **Model Context Protocol (MCP) Ready:** The server is configured to communicate via MCP, allowing it to be easily integrated and called as a tool by models in supported platforms.

---

## ⚙️ Installation

To run this project, you need Python and the required libraries.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/PavasKrishnanS/DataBro_using-MCP.git](https://github.com/PavasKrishnanS/DataBro_using-MCP.git)
    cd DataBro_using-MCP
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas matplotlib fastmcp
    ```

---

## 🚀 Usage

The server starts by running the main Python file. It will then listen for tool calls (e.g., from an integrating AI model like Claude) to execute the defined analysis functions.

### Running the Server

```bash
python data_server.py 
# Use the actual name of your script file if it's different.


## 🛠️ Core Technology Stack

* **FastMCP:** Framework for creating the tool server and exposing functions via the Model Context Protocol (MCP).
* **Context:** Developed and tested within the **Claude desktop environment** for seamless tool integration.
* **Pandas:** Data manipulation, cleaning, and summarization.
* **Matplotlib:** Data visualization engine.
* **Python's `base64` and `io` modules:** Used for encoding the resulting images.

