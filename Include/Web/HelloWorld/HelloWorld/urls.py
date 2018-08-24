from django.conf.urls import url

from.import view,testdb

urlpatterns = [
    url(r'^hello$',view.hello),
    url(r'^testdb_insert$',testdb.insert),
    url(r'^testdb_query$',testdb.query),
    url(r'^testdb_delete$',testdb.delete),
    url(r'^testdb_update$',testdb.update),
]