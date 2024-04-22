# Database Stress Test Utility

## Introduction (English)

This utility is designed to perform stress tests on SQL Server and Oracle databases by executing multiple CRUD operations in parallel threads. It ensures robust handling of database connections and operations to test the scalability and performance under heavy loads.

## 導入（日本語）

このユーティリティは、複数の CRUD 操作を並列スレッドで実行することにより、SQL Server および Oracle データベースのストレステストを行うために設計されています。データベース接続と操作の堅牢な処理を保証し、大量負荷下でのスケーラビリティとパフォーマンスをテストします。

## 簡介（正體中文）

此工具旨在通過並行執行多個 CRUD 操作來對 SQL Server 和 Oracle 資料庫進行壓力測試。它確保了數據庫連接和操作的堅固處理，以測試在重負荷下的可擴展性和性能。

## Features

- Supports both SQL Server and Oracle databases.
- Configurable number of threads and operations.
- Ensures database connectivity before initiating stress tests.
- Comprehensive error handling and logging.

## Setup

To set up the utility, clone this repository and install the necessary dependencies.

```bash
git clone https://github.com/your-github-username/your-repository.git
cd your-repository
# Install dependencies (if any)
```

## Configuration

Edit the `config_mssql.json` and `config_oracle.json` files to set your database connection parameters including server, user, password, and database details.

## Usage

Run the script corresponding to your database type:

For SQL Server:

```bash
python mssql.py
```

For Oracle:

```bash
python oracle.py
```

The scripts will perform the stress tests and provide a summary of the results including the total number of operations and the total time taken.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
