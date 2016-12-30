#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import MySQLdb



class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")


        conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd='123', db="db_house_price")
        cursor = conn.cursor()


        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

            cursor.execute('insert into test1 (url,title,summary) values (%s, %s,%s)',(data['url'].encode('utf-8'),data['title'].encode('utf-8'),data['summary'].encode('utf-8')))


        conn.commit()
        cursor.close()
        conn.close()


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()