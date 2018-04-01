from gluon.tools import Auth
import datetime

db = DAL('sqlite://storage.sqlite')
auth = Auth(db)

auth.settings.extra_fields['auth_user'] = [
    Field('utype', label='Sign up as'),
    Field('zipuserjournalist', label = 'Zipcode', comment = 'Journalists: Select your preferred zipcode and crimes in this region will be highlighted for you'),
    auth.signature]

auth.define_tables()


db.define_table(
    'crime',
    Field('crimetype', label = 'Type',  requires=IS_IN_SET(['Offence against a person', 'Violent offence', 'Sexual offence', 'Offence against property', 'Other'], zero = 'Choose one', error_message='Please select the incident type')),
    Field('incidentdate',  'datetime', label = 'Date'),
    Field('incidentlocation_1', comment='Please select the closest intersection street #1', label='Location - Intersection Street 1'),
    Field('incidentlocation_2', comment='Please select the closest intersection street #2', label='Location - Intersection Street 2'),
    Field('incidentZC', 'integer', label = 'Zipcode'),
    Field('incidentdesc', 'text', label = 'Description'),
    Field('journalistcomments', 'text', label = 'Closure Comments'),
    Field('status', requires=IS_IN_SET(['Open', 'In Progress', 'Completed']), default='Open'),
    Field('attachmentreguser','upload', label = 'User Attachment', comment='Please upload a zip file if you have more than one file'),
    Field('attachmentjournalist','upload', label = 'Journalist Attachment', comment='Please upload a zip file if you have more than one file'),
    Field('journalistincharge', 'reference auth_user'),
    auth.signature)

db.define_table(
    'allzipcodes',
    Field('allcode', 'integer', unique=True)
)

db.crime.incidentZC.requires = IS_IN_DB(db, db.allzipcodes.allcode, '', zero ='Choose one', error_message='Please select the incident zipcode')
db.auth_user.zipuserjournalist.requires = IS_IN_DB(db, db.allzipcodes.allcode, '', zero ='Choose one', error_message='Please select your zipcode')
db.auth_user.utype.requires = IS_IN_SET(['Regular User', 'Journalist'],zero='Choose one', error_message= 'Please select a user type')
db.crime.incidentdate.requires = IS_DATETIME_IN_RANGE(minimum=datetime.datetime(2008,1,1,10,30),
                                                maximum=datetime.datetime.today(),
                                                error_message='Dates cannot be future dates')


# db.allzipcodes.insert(allcode="60601")
# db.allzipcodes.insert(allcode="60602")
# db.allzipcodes.insert(allcode="60603")
# db.allzipcodes.insert(allcode="60604")
# db.allzipcodes.insert(allcode="60605")
# db.allzipcodes.insert(allcode="60606")
# db.allzipcodes.insert(allcode="60607")
# db.allzipcodes.insert(allcode="60608")
# db.allzipcodes.insert(allcode="60609")
# db.allzipcodes.insert(allcode="60610")
# db.allzipcodes.insert(allcode="60611")
# db.allzipcodes.insert(allcode="60612")
# db.allzipcodes.insert(allcode="60613")
# db.allzipcodes.insert(allcode="60614")
# db.allzipcodes.insert(allcode="60615")
# db.allzipcodes.insert(allcode="60616")
# db.allzipcodes.insert(allcode="60617")
# db.allzipcodes.insert(allcode="60618")
# db.allzipcodes.insert(allcode="60619")
# db.allzipcodes.insert(allcode="60620")
# db.allzipcodes.insert(allcode="60621")
# db.allzipcodes.insert(allcode="60622")
# db.allzipcodes.insert(allcode="60623")
# db.allzipcodes.insert(allcode="60624")
# db.allzipcodes.insert(allcode="60625")
# db.allzipcodes.insert(allcode="60626")
# db.allzipcodes.insert(allcode="60627")
# db.allzipcodes.insert(allcode="60628")
# db.allzipcodes.insert(allcode="60629")
# db.allzipcodes.insert(allcode="60630")
# db.allzipcodes.insert(allcode="60631")
# db.allzipcodes.insert(allcode="60632")
# db.allzipcodes.insert(allcode="60633")
# db.allzipcodes.insert(allcode="60634")
# db.allzipcodes.insert(allcode="60635")
# db.allzipcodes.insert(allcode="60636")
# db.allzipcodes.insert(allcode="60637")
# db.allzipcodes.insert(allcode="60638")
# db.allzipcodes.insert(allcode="60639")
# db.allzipcodes.insert(allcode="60640")
# db.allzipcodes.insert(allcode="60641")
# db.allzipcodes.insert(allcode="60642")
# db.allzipcodes.insert(allcode="60643")
# db.allzipcodes.insert(allcode="60644")
# db.allzipcodes.insert(allcode="60645")
# db.allzipcodes.insert(allcode="60646")
# db.allzipcodes.insert(allcode="60647")
# db.allzipcodes.insert(allcode="60648")
# db.allzipcodes.insert(allcode="60649")
# db.allzipcodes.insert(allcode="60650")
# db.allzipcodes.insert(allcode="60651")
# db.allzipcodes.insert(allcode="60652")
# db.allzipcodes.insert(allcode="60653")
# db.allzipcodes.insert(allcode="60654")
# db.allzipcodes.insert(allcode="60655")
# db.allzipcodes.insert(allcode="60656")
# db.allzipcodes.insert(allcode="60657")
# db.allzipcodes.insert(allcode="60658")
# db.allzipcodes.insert(allcode="60659")
# db.allzipcodes.insert(allcode="60660")
# db.allzipcodes.insert(allcode="60661")
# db.allzipcodes.insert(allcode="60662")
# db.allzipcodes.insert(allcode="60663")
# db.allzipcodes.insert(allcode="60664")
# db.allzipcodes.insert(allcode="60665")
# db.allzipcodes.insert(allcode="60666")
# db.allzipcodes.insert(allcode="60667")
# db.allzipcodes.insert(allcode="60668")
# db.allzipcodes.insert(allcode="60669")
# db.allzipcodes.insert(allcode="60670")
# db.allzipcodes.insert(allcode="60671")
# db.allzipcodes.insert(allcode="60672")
# db.allzipcodes.insert(allcode="60673")
# db.allzipcodes.insert(allcode="60674")
# db.allzipcodes.insert(allcode="60675")
# db.allzipcodes.insert(allcode="60676")
# db.allzipcodes.insert(allcode="60677")
# db.allzipcodes.insert(allcode="60678")
# db.allzipcodes.insert(allcode="60679")
# db.allzipcodes.insert(allcode="60680")
# db.allzipcodes.insert(allcode="60681")
# db.allzipcodes.insert(allcode="60682")
# db.allzipcodes.insert(allcode="60683")
# db.allzipcodes.insert(allcode="60684")
