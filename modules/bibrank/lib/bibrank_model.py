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
bibrank database models.
"""

# General imports.
from invenio.sqlalchemyutils import db

# Create your models here.

from websession_model import User
from bibedit_model import Bibrec, Bibdoc

class RnkMETHOD(db.Model):
    """Represents a RnkMETHOD record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkMETHOD'
    id = db.Column(db.MediumInteger(9, unsigned=True), primary_key=True,
                nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False,
                server_default='')
    last_updated = db.Column(db.DateTime, nullable=False,
        server_default='0000-00-00 00:00:00')

class RnkMETHODDATA(db.Model):
    """Represents a RnkMETHODDATA record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkMETHODDATA'
    id_rnkMETHOD = db.Column(db.MediumInteger(9, unsigned=True),
                db.ForeignKey(RnkMETHOD.id), nullable=False, primary_key=True)
    relevance_data = db.Column(db.iLargeBinary, nullable=True)

class RnkMETHODNAME(db.Model):
    """Represents a RnkMETHODNAME record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkMETHODNAME'
    id_rnkMETHOD = db.Column(db.MediumInteger(9, unsigned=True),
                db.ForeignKey(RnkMETHOD.id), primary_key=True)
    ln = db.Column(db.Char(5), primary_key=True,
                server_default='')
    type = db.Column(db.Char(3), primary_key=True,
                server_default='sn')
    value = db.Column(db.String(255), nullable=False)
    method = db.relationship(RnkMETHOD, backref='names')

class RnkCITATIONDATA(db.Model):
    """Represents a RnkCITATIONDATA record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkCITATIONDATA'
    id = db.Column(db.MediumInteger(8, unsigned=True), primary_key=True,
                nullable=False)
    object_name = db.Column(db.String(20), unique=True,
                nullable=False)
    object_value = db.Column(db.iLargeBinary, nullable=True)
    last_updated = db.Column(db.DateTime, nullable=False,
        server_default='0000-00-00 00:00:00')


class RnkCITATIONDATAEXT(db.Model):
    """Represents a RnkCITATIONDATAEXT record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkCITATIONDATAEXT'
    id_bibrec = db.Column(db.Integer(8, unsigned=True),
                db.ForeignKey(Bibrec.id),
            primary_key=True, nullable=False,
                server_default='0')
    extcitepubinfo = db.Column(db.String(255), primary_key=True,
                nullable=False,
            index=True)

class RnkAUTHORDATA(db.Model):
    """Represents a RnkAUTHORDATA record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkAUTHORDATA'
    aterm = db.Column(db.String(50), primary_key=True,
                nullable=True)
    hitlist = db.Column(db.iLargeBinary, nullable=True)

class RnkDOWNLOADS(db.Model):
    """Represents a RnkDOWNLOADS record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkDOWNLOADS'
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                autoincrement=True)
    id_bibrec = db.Column(db.MediumInteger(8, unsigned=True),
                db.ForeignKey(Bibrec.id), nullable=True)
    download_time = db.Column(db.DateTime, nullable=True,
            server_default='0000-00-00 00:00:00')
    client_host = db.Column(db.Integer(10, unsigned=True),
                nullable=True)
    id_user = db.Column(db.Integer(15, unsigned=True), db.ForeignKey(User.id),
                nullable=True)
    id_bibdoc = db.Column(db.MediumInteger(9, unsigned=True),
                db.ForeignKey(Bibdoc.id), nullable=True)
    file_version = db.Column(db.SmallInteger(2, unsigned=True),
                nullable=True)
    file_format = db.Column(db.String(10), nullable=True)
    bibrec = db.relationship(Bibrec, backref='downloads')
    bibdoc = db.relationship(Bibdoc, backref='downloads')
    user = db.relationship(User, backref='downloads')

class RnkPAGEVIEWS(db.Model):
    """Represents a RnkPAGEVIEWS record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkPAGEVIEWS'
    id = db.Column(db.MediumInteger, primary_key=True,
                nullable=False,
                autoincrement=True)
    id_bibrec = db.Column(db.MediumInteger(8, unsigned=True),
                db.ForeignKey(Bibrec.id), nullable=True,
            primary_key=True)
    id_user = db.Column(db.Integer(15, unsigned=True),
                db.ForeignKey(User.id),
            server_default='0', primary_key=True)
    client_host = db.Column(db.Integer(10, unsigned=True),
                nullable=True)
    view_time = db.Column(db.DateTime, primary_key=True,
            server_default='0000-00-00 00:00:00')
    bibrec = db.relationship(Bibrec, backref='pageviews')
    user = db.relationship(User, backref='pageviews')

class RnkWORD01F(db.Model):
    """Represents a RnkWORD01F record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkWORD01F'
    id = db.Column(db.MediumInteger(9, unsigned=True), nullable=False,
                primary_key=True,
                autoincrement=True)
    term = db.Column(db.String(50), nullable=True)
    hitlist = db.Column(db.iLargeBinary, nullable=True)

class RnkWORD01R(db.Model):
    """Represents a RnkWORD01R record."""
    def __init__(self):
        pass
    __tablename__ = 'rnkWORD01R'
    id_bibrec = db.Column(db.MediumInteger(9, unsigned=True),
                db.ForeignKey(Bibrec.id), nullable=False, primary_key=True)
    termlist = db.Column(db.iLargeBinary, nullable=True)
    type = db.Column(db.Enum('CURRENT', 'FUTURE', 'TEMPORARY'),
                nullable=False,
            server_default='CURRENT', primary_key=True)
    bibrec = db.relationship(Bibrec, backref='word01rs')

