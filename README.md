municipios-provincias-comunidades-INE-spain
===========================================

SQL dump and relationship between municipalities, provinces and Spanish autonomous communities

Main source: http://www.ine.es/jaxi/menu.do?type=pcaxis&path=%2Ft20%2Fe245%2Fcodmun%2F&file=inebase&L=0

==Dependencies==

Only for run the python Excel parser you need:

  $ sudo pip install pandas xlrd sqlalchemy


==Generate new SQL dump for municipalities==

For generate .sqlite file from INE's excel file

  $ python3 municipalities_parser.py 

To export sqlite to SQL run:

  $ sqlite3 municipalities_spain.sqlite .dump > municipalities_spain_aux.sql
