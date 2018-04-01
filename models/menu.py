# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('LogIt'),
                  _class="navbar-brand",
                  )
#response.title = request.application.replace('_', ' ').title()
response.title = 'LogIt'
response.subtitle = 'Help other Chicagoans'

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------


    if auth.user:
        usertype = auth.user.utype
    else:
        usertype = 'None'

    response.menu.append((T("Log an incident"), False, URL('default', 'loganincident')))

    if usertype == 'Regular User':
        response.menu.append((T("My incidents"), False, URL('default', 'mycrime_regularuser')))
    elif usertype == 'Journalist':
        response.menu += [(T("All Incidents"), False, '#',[
                             (T('My Incidents'), False,
                              URL('default', 'mycrime_journalist')),
                             (T('Other Incidents'), False,
                              URL('default', 'othercrime_journalist')),
                            ])
                        ]

if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
