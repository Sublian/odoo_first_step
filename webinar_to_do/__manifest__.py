{
    'name':'Webinar To Do',
    'version': '1.0',
    'summary': 'Gestión simple de tareas',
    'category': 'Productivity',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': ['views/views.xml', 'security/ir.model.access.csv'],
    'assets': {
        'web.assets_backend': [
            'webinar_to_do/static/src/css/webinar_to_do.css',
        ],
    },
    'installable': True,
    'application': True,
}