import cx_Oracle
import json
from threading import Thread
import time

def execute_query(cursor, query):
    try:
        cursor.execute(query)
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            return "Query executed successfully."
    except Exception as e:
        print(f"執行查詢時發生錯誤: {str(e)}")
        return None

def test_database_connection(dsn, user, password):
    """嘗試連接到資料庫，確認是否可連接"""
    try:
        with cx_Oracle.connect(user, password, dsn, encoding="UTF-8"):
            print("資料庫連接成功，開始進行壓力測試。")
            return True
    except Exception as e:
        print(f"無法連接到資料庫: {str(e)}")
        return False

def perform_crud_operations(dsn, user, password, thread_id, num_operations):
    try:
        with cx_Oracle.connect(user, password, dsn, encoding="UTF-8") as connection:
            cursor = connection.cursor()
            for i in range(num_operations):
                execute_query(cursor, f"INSERT INTO ExampleTable (id, data) VALUES ({1000 * thread_id + i}, 'Data {i}')")
                execute_query(cursor, f"SELECT * FROM ExampleTable WHERE id = {1000 * thread_id + i}")
                execute_query(cursor, f"UPDATE ExampleTable SET data = 'Updated Data {i}' WHERE id = {1000 * thread_id + i}")
                execute_query(cursor, f"DELETE FROM ExampleTable WHERE id = {1000 * thread_id + i}")
            connection.commit()
    except Exception as e:
        print(f"線程 {thread_id}: 資料庫操作時出錯: {str(e)}")

def main():
    with open('config_oracle.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    dsn = cx_Oracle.makedsn(config['host'], config['port'], service_name=config['service_name'])

    # 先測試資料庫連接是否成功
    if not test_database_connection(dsn, config['user'], config['password']):
        print("由於無法連接到資料庫，壓力測試不會執行。")
        return

    num_threads = 10
    operations_per_thread = 100

    threads = []
    start_time = time.time()

    for i in range(num_threads):
        thread = Thread(target=perform_crud_operations, args=(dsn, config['user'], config['password'], i, operations_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_operations = num_threads * operations_per_thread

    print("Oracle 壓力測試結果總結：")
    print(f"測試配置：{num_threads} 個線程，每個線程執行 {operations_per_thread} 次 CRUD 操作。")
    print(f"總操作次數：{total_operations} 次")
    print(f"總耗時：{end_time - start_time:.2f} 秒")

if __name__ == '__main__':
    main()
