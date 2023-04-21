# 7. Conexión con bases de datos (DB-API)

## Índice

[1. Fundamentos de bases de datos relacionales](#1-fundamentos-de-bases-de-datos-relacionales)  
[2. DB-API](#2-db-api)

## 1. Fundamentos de bases de datos relacionales

.

## 2. DB-API

Para trabajar con bases de datos, Python dispone de varios paquetes de terceros a instalar, que incluyen los llamados conectores, y que dependen del sistema gestor de base de datos (SGBD) con el que se quiera trabajar: MySQL, PosgreSQL, SQL Server, Oracle, etc., en el caso de relacionales, y MongoDB, etc., en el caso de NoSQL.

Sea cual sea el que se elija, implica también instalar en la máquina el SGBD en cuestión y tener un servidor activo y escuchando, configurado y listo para aceptar peticiones de la aplicación que estamos desarrollando, salvo que ya se disponga previamente de un servidor de base de datos levantado (sea un servicio en la nube de terceros o un servidor propio).

Además, desde la versión 2.5, Python incluye un gestor de SQLite integrado, que para pruebas en desarrollo puede resultar bastante útil sin necesidad de instalar un SGBD.

El siguiente es un ejemplo básico completo de creación de base de datos con creación de una tabla, población de datos y obtención de datos:

    import sqlite3

    database = sqlite3.connect("example.db")
    cursor = database.cursor()

    def createTable():
      global cursor

      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS books(
            id INT PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            author VARCHAR(50) NOT NULL,
            genre VARCHAR(20) NULL,
            cost REAL NOT NULL
          );
        """
      )

    def populateData():
      global database
      global cursor

      cursor.execute(
        """
          INSERT INTO books
          VALUES
            (1, 'Los pilares de la tierra', 'Ken Follet', 'Suspense', 45),
            (2, 'Entrevista con el vampiro', 'Anne Rice', 'Fantasía', 25);
        """
      )

      database.commit()

    def selectData():
      global cursor

      cursor.execute(
        """
          SELECT *
            FROM books;
        """
      )

      return cursor.fetchall()

    # -------------------

    createTable()
    populateData()

    books = selectData()

    print(books)

## Referencias

[Bases de datos relacionales I](https://datamanagement.es/2020/03/30/fundamentos-de-las-bases-de-datos-relacionales-para-data-science-y-dummies/)  
[Bases de datos relacionales II](https://www.ionos.es/digitalguide/hosting/cuestiones-tecnicas/bases-de-datos-relacionales/)  
[w3schools MySQL](https://www.w3schools.com/mysql/)  
[Python DB-API: MySQLdb](https://www.tutorialspoint.com/python/python_database_access.htm)  
[MySQL server](https://dev.mysql.com/downloads/installer/)  
[Python MySQL connector](https://dev.mysql.com/downloads/connector/python/)  
[Introducción a SQLite con Python](https://parzibyte.me/blog/2017/11/21/python-3-sqlite-3-introduccion-ejemplos/)  
[Manual de SQLite](https://www.geeksforgeeks.org/python-sqlite/)  
[Tutorial MySQL Python](https://www.w3schools.com/python/python_mysql_getstarted.asp)  
[db4free](https://www.db4free.net/)