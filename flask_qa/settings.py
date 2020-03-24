import os

#credentials for connecting to pgadmin
POSTGRES = {
    'user' : 'prbxpoeaihkxly',
    'pw' : 'f83c6578489316eb2387f126f47bea98398521aa4e74f4b4e5f0de06f48746f7',
    'db' : 'd2k8ntsq38d25h',
    'host' : 'ec2-50-17-178-87.compute-1.amazonaws.com',
    'port' : '5432',
}


#if using local db:
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#if using production/pgadmin db:
SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s"

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
