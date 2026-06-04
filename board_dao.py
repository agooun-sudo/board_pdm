import pymysql # sql 에서 

class BoardDAO:
    
    def __init__(self):
        self.host = "localhost"
        self.user = "board_user"
        self.password = "board1234"
        self.database = "board_db"

    def get_connection(self):#커넥션 db접속을 연결해주는
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8mb4'
        )

    def select_all(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        select *
        from board
        order by id asc
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
    
        return result
    
    def insert(self, title, content, writer):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        insert into board (title, content, writer)
        values (%s, %s, %s)
        """

        cursor.execute(sql, (title, content, writer))
        conn.commit()
        cursor.close()
        conn.close()
    
    def select_one(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM board
        WHERE id=%s
        """

        
        cursor.execute(sql, (board_id,))
        result = cursor.fetchone()
        print(result)
        cursor.close()
        conn.close()

         return result
    
    def delete_board(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))

        conn.commit()

        cursor.close()
        conn.close()

        print("삭제 완료")