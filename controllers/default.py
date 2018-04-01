from gluon.tools import Crud
crud = Crud(db)

if auth.user:
    usertype = auth.user.utype
else:
    usertype = 'None'

auth.requires_login_or_token()
def index():

    return {}

@auth.requires_login()
def loganincident():
    db.crime.status.writable = False
    db.crime.journalistincharge.writable = False
    db.crime.journalistincharge.readable = False
    db.crime.attachmentjournalist.writable = False
    db.crime.attachmentjournalist.readable = False
    db.crime.journalistcomments.writable = False
    db.crime.journalistcomments.readable = False

    db.crime.incidentlocation_1.requires = IS_NOT_EMPTY(error_message="Street 1 is required")
    db.crime.incidentlocation_2.requires = IS_NOT_EMPTY(error_message="Street 2 is required")
    db.crime.incidentdesc.requires = IS_NOT_EMPTY(error_message="Incident description is required")

    form = SQLFORM(db.crime, request.vars.id).process()

    if form.accepted:
        if usertype == 'Regular User':
            redirect(URL('mycrime_regularuser'))
        elif usertype == 'Journalist':
            redirect(URL('mycrime_journalist'))
        else:
            redirect(URL('index'))

    grid = SQLFORM.grid(db.crime, csv=False, searchable=False, editable=False, deletable=False)

    return {'form': form, 'grid': grid}

@auth.requires_login()
@auth.requires(usertype == 'Regular User')
def mycrime_regularuser():
    db.crime.journalistincharge.writable = False
    db.crime.journalistincharge.readable = False
    db.crime.attachmentjournalist.readable = False
    db.crime.attachmentjournalist.writable = False
    db.crime.attachmentreguser.readable = False
    db.crime.attachmentreguser.writable = False
    db.crime.journalistcomments.readable = False
    db.crime.journalistcomments.writable = False

    links = [lambda row: A('View Incident', _href=URL("default", "viewCrime", args=[row.id]))]
    db.crime.id.readable = False

    myopenquery = db.crime.created_by == auth.user_id
    myopenquery &= db.crime.status == 'Open'

    myopenincidentsgrid = SQLFORM.grid(myopenquery, csv=False, onupdate=myonupdate,
                                          deletable=True, editable=False, searchable=False, details=False, paginate=5,
                                          create=False,
                                          links=links, orderby=~db.crime.created_on)
    myinprogressquery = db.crime.created_by == auth.user_id
    myinprogressquery &= db.crime.status == 'In Progress'
    myinprogressincidentsgrid = SQLFORM.grid(myinprogressquery, csv=False, onupdate=myonupdate,
                                          deletable=False, editable=False, searchable=False, details=False, paginate=5,
                                          create=False,
                                          links=links, orderby=~db.crime.created_on)

    myclosedincquery = db.crime.created_by == auth.user_id
    myclosedincquery &= db.crime.status == 'Completed'
    myclosedincidentsgrid = SQLFORM.grid(myclosedincquery, csv=False, onupdate=myonupdate,
                                         deletable=False, editable=False, searchable=False, details=False, paginate=5,
                                         create=False,
                                         links=links, orderby=~db.crime.created_on)

    return {'myopenincidentsgrid': myopenincidentsgrid, 'myinprogressincidentsgrid': myinprogressincidentsgrid,
             'myclosedincidentsgrid': myclosedincidentsgrid}

@auth.requires_login()
@auth.requires(usertype == 'Journalist')
def mycrime_journalist():
    db.crime.journalistincharge.writable = False
    db.crime.journalistincharge.readable = False
    db.crime.attachmentjournalist.readable = False
    db.crime.attachmentjournalist.writable = False
    db.crime.attachmentreguser.readable = False
    db.crime.attachmentreguser.writable = False
    db.crime.journalistcomments.readable = False
    db.crime.journalistcomments.writable = False

    links = [lambda row: A('View Incident', _href=URL("default", "viewCrime", args=[row.id]))]
    db.crime.id.readable = False
    mycreatedincidentsgrid = SQLFORM.grid(db.crime.created_by == auth.user_id, csv=False, onupdate=myonupdate,
                                          deletable=True, editable=False, searchable= False, details=False, paginate=5, create=False,
                                          links=links, orderby=~db.crime.created_on)
    myworkingquery = db.crime.journalistincharge == auth.user_id
    myworkingquery &= db.crime.status == 'In Progress'
    myworkingincidentsgrid = SQLFORM.grid(myworkingquery, csv=False, onupdate=myonupdate,
                                          deletable=False, editable=False, searchable= False, details=False, paginate=5, create=False,
                                          links=links, orderby=~db.crime.created_on)

    myclosedincquery = db.crime.journalistincharge == auth.user_id
    myclosedincquery &= db.crime.status == 'Completed'
    myclosedincidentsgrid = SQLFORM.grid(myclosedincquery, csv=False, onupdate=myonupdate,
                                          deletable=False, editable=False, searchable= False, details=False, paginate=5, create=False,
                                          links=links, orderby=~db.crime.created_on)

    return{'mycreatedincidentsgrid':mycreatedincidentsgrid,'myworkingincidentsgrid':myworkingincidentsgrid, 'myclosedincidentsgrid': myclosedincidentsgrid}

@auth.requires_login()
@auth.requires(usertype == 'Journalist')
def othercrime_journalist():
    db.crime.journalistincharge.writable = False
    db.crime.journalistincharge.readable = False
    db.crime.attachmentjournalist.readable = False
    db.crime.attachmentjournalist.writable = False
    db.crime.attachmentreguser.readable = False
    db.crime.attachmentreguser.writable = False
    db.crime.journalistcomments.readable = False
    db.crime.journalistcomments.writable = False
    db.crime.id.readable = False
    links = [lambda row: A('View Incident', _href=URL("default", "viewCrime", args=[row.id]))]


    querypreferredzip = db.crime.created_by != auth.user_id
    querypreferredzip &= db.crime.status == 'Open'
    querypreferredzip &= db.crime.incidentZC == auth.user.zipuserjournalist
    preferredzipcodeincidentsgrid = SQLFORM.grid(
        querypreferredzip, csv=False, onupdate=myonupdate,
        deletable=False, searchable= False, editable=False, details=False, paginate=5, create=False,
        links=links, orderby=~db.crime.created_on)

    allotherincidentsquery = db.crime.created_by != auth.user.id
    allotherincidentsquery &= db.crime.status == 'Open'
    allotherincidentsquery &= db.crime.incidentZC != auth.user.zipuserjournalist

    allotherincidentsgrid = SQLFORM.grid(
        allotherincidentsquery, csv=False,
        onupdate=myonupdate,
        deletable=False, editable=False, searchable= False, details=False, paginate=5, create=False,
        links=links, orderby=~db.crime.created_on)

    return{'preferredzipcodeincidentsgrid':preferredzipcodeincidentsgrid,'allotherincidentsgrid':allotherincidentsgrid}

@auth.requires_login()
def viewCrime():
    rows = db(db.crime.id == request.args(0)).select()
    return {'rows': rows}

def myonupdate(form):
    db(db['crime']._id == request.vars.id).update(**{'journalistincharge': auth.user.id})

@auth.requires_login()
@auth.requires(usertype == 'Journalist')
def formonupdate():
    db(db['crime']._id == request.args(0)).update(**{'journalistincharge': auth.user.id, 'status':'In Progress'})

@auth.requires_login()
@auth.requires(usertype == 'Journalist')
def leaveincident():
    db(db['crime']._id == request.args(0)).update(**{'journalistincharge': '', 'status':'Open'})

# @auth.requires_login()
# @auth.requires(usertype == 'Journalist')
# def emailjournalist():
#     row = db(db.crime.id == request.args(0)).select()
#     email = row.journalistincharge.email
#     auth.mailer.send(to=email, subject='Alert from LogIt',
#                      message='%s is requesting to follow a case you are following : ' % auth.user.first_name)

@auth.requires_login()
@auth.requires(usertype == 'Journalist')
def closeincident():
    record = db.crime(request.args(0)) or redirect(URL('index'))

    fields = ['journalistcomments', 'attachmentjournalist']

    buttons = [TAG.button('Close Incident', _type="submit"),
               TAG.button('Back', _type="button", _onClick="parent.location='%s' " % URL('default', 'viewCrime', args=[request.args(0)]))]

    db.crime.journalistcomments.requires = IS_NOT_EMPTY(error_message='Closure comments are required before you close an incident')
    db.crime.attachmentjournalist.requires = IS_NOT_EMPTY(error_message='Closure attachment is required before you close an incident')
    closureform = SQLFORM(db.crime, record, fields=fields, buttons=buttons)

    if closureform.process().accepted:
        response.flash = 'Incident Closed'
        db(db['crime']._id == request.args(0)).update(**{'status': 'Completed'})
        redirect(URL('mycrime_journalist'))
    elif closureform.errors:
        response.flash = 'Error! Please check the form'
    else:
        response.flash = 'Please fill out the form'
    return{'closureform': closureform}

def user():

    return dict(form=auth())

@cache.action()
def download():

    return response.download(request, db)


def call():

    return service()


