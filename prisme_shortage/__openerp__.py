{
'name': 'Prisme Shortage',
'version': '2017-08-17 09:15',
'category': 'Warehouse',
'summary': 'products shortage',
'author': 'Prisme Solutions Informatique SA',
'website': 'http://www.prisme.ch',
'depends': ['base', 'account', 'sale', 'stock', ],
'init_xml': [],
'update_xml': [
    'security/ir.model.access.csv',
    'shortage_view.xml',
],
'demo_xml': [],
'installable': True,
'active': False,
'images': [
           'images/shortage.jpg',
           ],
}
