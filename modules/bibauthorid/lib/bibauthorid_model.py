# -*- coding: utf-8 -*-
#
## Author: Jiri Kuncar <jiri.kuncar@gmail.com> 
##
## This file is part of Invenio.
## Copyright (C) 2011, 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""
bibauthorid database models.
"""

# General imports.
from invenio.sqlalchemyutils import db

# Create your models here.

#FIX ME Add db.relationships

class AidAUTHORNAMES(db.Model):
    """Represents a AidAUTHORNAMES record."""
    def __init__(self):
        pass
    __tablename__ = 'aidAUTHORNAMES'
    __table_args__ = {'useexisting':True}#, 'extend_existing': True}
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    Name = db.Column(db.String(255), nullable=False,
                index=True)
    bibrefs = db.Column(db.String(200), nullable=False,
                index=True)
    db_name = db.Column(db.String(255), nullable=True,
                index=True)

class AidAUTHORNAMESBIBREFS(db.Model):
    """Represents a AidAUTHORNAMESBIBREFS record."""
    def __init__(self):
        pass
    __tablename__ = 'aidAUTHORNAMESBIBREFS'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    Name_id = db.Column(db.BigInteger(15), nullable=False,
                index=True)
    bibref = db.Column(db.String(200), nullable=False,
                index=True)

class AidCACHE(db.Model):
    """Represents a AidCACHE record."""
    def __init__(self):
        pass
    __tablename__ = 'aidCACHE'
    id = db.Column(db.Integer(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    object_name = db.Column(db.String(120), nullable=False,
                index=True)
    object_key = db.Column(db.String(120), nullable=False,
                index=True)
    object_value = db.Column(db.Text, nullable=True)
    last_updated = db.Column(db.DateTime, nullable=False,
                index=True)


class AidDOCLIST(db.Model):
    """Represents a AidDOCLIST record."""
    def __init__(self):
        pass
    __tablename__ = 'aidDOCLIST'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    bibrecID = db.Column(db.BigInteger(15), nullable=False,
                index=True)
    processed_author = db.Column(db.BigInteger(15), nullable=True,
                index=True)

class AidPERSONID(db.Model):
    """Represents a AidPERSONID record."""
    def __init__(self):
        pass
    __tablename__ = 'aidPERSONID'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    personid = db.Column(db.BigInteger(15), nullable=False,
                index=True)
    tag = db.Column(db.String(50), nullable=False,
                index=True)
    data = db.Column(db.String(250), nullable=False,
                index=True)
    flag = db.Column(db.Integer(11), nullable=False, server_default='0',
                index=True)
    lcul = db.Column(db.Integer(11), nullable=False, server_default='0',
                index=True)
    #__table_args__ = {#'indexes': (db.Index('tdf-b', tag, data, flag),
    #                  #            db.Index('ptf-b', personid, data, flag)),
    #                  'extend_existing': True}

class AidREALAUTHORDATA(db.Model):
    """Represents a AidREALAUTHORDATA record."""
    def __init__(self):
        pass
    __tablename__ = 'aidREALAUTHORDATA'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    realauthorID = db.Column(db.BigInteger(15), nullable=False)
    tag = db.Column(db.String(50), nullable=False,
                index=True)
    value = db.Column(db.String(255), nullable=False,
                index=True)
    va_count = db.Column(db.Integer(8), nullable=False,
                server_default='0')
    va_names_p = db.Column(db.Double, nullable=False,
                server_default='0')
    va_p = db.Column(db.Double, nullable=False, server_default='0')
    #__table_args__ = (db.Index('realauthorID-b', realauthorID, tag),
    #            {})


class AidUSERINPUTLOG(db.Model):
    """Represents a AidUSERINPUTLOG record."""
    def __init__(self):
        pass
    __tablename__ = 'aidUSERINPUTLOG'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    transactionid = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
            autoincrement=True, index=True)
    timestamp = db.Column(db.DateTime, nullable=False,
                index=True)
    userinfo = db.Column(db.String(255), nullable=False,
                index=True)
    personid = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
            autoincrement=True, index=True)
    action = db.Column(db.String(50), nullable=False,
                index=True)
    tag = db.Column(db.String(50), nullable=False,
                index=True)
    value = db.Column(db.String(200), nullable=False,
                index=True)
    comment = db.Column(db.Text, nullable=True)

class AidVIRTUALAUTHORS(db.Model):
    """Represents a AidVIRTUALAUTHORS record."""
    def __init__(self):
        pass
    __tablename__ = 'aidVIRTUALAUTHORS'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    virtualauthorID = db.Column(db.BigInteger(15),
                db.ForeignKey(AidAUTHORNAMES.id),
            nullable=False, index=True)
    authornamesID = db.Column(db.BigInteger(15), nullable=False,
                index=True)
    p = db.Column(db.Float, nullable=False)
    clusterID = db.Column(db.BigInteger(15), nullable=False,
                server_default='0',
            index=True)

class AidVIRTUALAUTHORSCLUSTERS(db.Model):
    """Represents a AidVIRTUALAUTHORSCLUSTERS record."""
    def __init__(self):
        pass
    __tablename__ = 'aidVIRTUALAUTHORSCLUSTERS'
    id = db.Column(db.Integer(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    cluster_name = db.Column(db.String(60), nullable=False)

class AidVIRTUALAUTHORSDATA(db.Model):
    """Represents a AidVIRTUALAUTHORSDATA record."""
    def __init__(self):
        pass
    __tablename__ = 'aidVIRTUALAUTHORSDATA'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    virtualauthorID = db.Column(db.BigInteger(15),
                db.ForeignKey(AidVIRTUALAUTHORS.id),
            nullable=False, index=True)
    tag = db.Column(db.String(255), nullable=False,
                index=True)
    value = db.Column(db.String(255), nullable=False,
                index=True)

class AidREALAUTHORS(db.Model):
    """Represents a AidREALAUTHORS record."""
    def __init__(self):
        pass
    __tablename__ = 'aidREALAUTHORS'
    id = db.Column(db.BigInteger(15), nullable=False,
                primary_key=True,
                autoincrement=True)
    realauthorID = db.Column(db.BigInteger(15), nullable=False,
                index=True)
    virtualauthorID = db.Column(db.BigInteger(15),
                db.ForeignKey(AidVIRTUALAUTHORS.id),
            nullable=False, index=True)
    p = db.Column(db.Float, nullable=False)

