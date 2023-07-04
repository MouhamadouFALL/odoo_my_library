# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
            Manage Library
            ==============
            Description related to library.
        """,  # Supports reStructuredText(RST) format
    'author': "MouhamadouFALL",
    'website': "http://www.siggiDieuf.com",
    'category': 'Library/',
    'version': '15.0.1.0.0',
    'depends': ['base',],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'views/library_book_menu.xml',
    ],
    'application': True,
    'installable': True,

    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],

}




