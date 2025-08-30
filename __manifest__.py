{
    'name': 'Gestión de Incidentes de Seguridad',
    'version': '1.0',
    'category': 'Ciberseguridad',
    'description': 'Módulo CRUD para la gestión de incidentes de seguridad',
    'author': 'Erick Hernández',
    'website': 'http://localhost:8069',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Permisos de acceso
        'views/incidentes_views.xml',  # Vistas del módulo
    ],
    'installable': True,
    'auto_install': False,
    'icon': '/mi_modulo/static/description/icon.png',
}
