# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Your Company
#    Copyright (C) 2004-TODAY Your tommy.yu(tommy.ywt@gmail.com).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
{
    'name': 'wkf_msg',
    'version': '1.0',
    'category': '',
    "sequence": 20,
    'complexity': "easy",
    'description': """
    """,
    'author': 'tommy.yu',
    'website': 'http://104.160.32.19',
    'images': [],
    'depends': [],
    'init_xml': [],
    'update_xml': [
        'wkf_message_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'test': [

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
