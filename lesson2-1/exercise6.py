# Level 3
# sixth exercise

db = ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
properties = ('dialect', 'host', 'port', 'database name', 'user name', 'password')

# create production db config dict with zip
prod_config = dict(zip(properties, db))
print "Production database connection properties: \n", format(prod_config) + "\n"

## or create production db config dict with map
#dblist = list(db)
#proplist = list(properties)

#prod_config = dict(list(map(None, proplist, dblist)))
#print "Production database connection properties: \n", format(prod_config) + "\n"

# copy production db config to staging dict
staging_config = prod_config.copy()
print "Staging database connection properties: \n", format(staging_config) + "\n"

# update host and password
staging_config.update({'host': 'semantic.amazonaws-staging.com', 'password': 'root'})
print "Updated staging atabase connection properties: \n", format(staging_config) + "\n"

# format output string
print ("prod_config: {dialect}://{username}:{password}@{host}:{port}/{databasename}".format(dialect=prod_config.get('dialect'), username=prod_config.get('user name'),
password=prod_config.get('password'), host=prod_config.get('host'), port=prod_config.get('port'), databasename=prod_config.get('database name')))

print ("staging_config: {dialect}://{username}:{password}@{host}:{port}/{databasename}".format(dialect=staging_config.get('dialect'), username=staging_config.get('user name'),
password=staging_config.get('password'), host=staging_config.get('host'), port=staging_config.get('port'), databasename=staging_config.get('database name')))


