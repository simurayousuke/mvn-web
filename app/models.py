# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, ForeignKey, Index, Integer, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class M2Dependency(Base):
    __tablename__ = 'm2_dependency'

    id = Column(Integer, primary_key=True, server_default=text("nextval('m2_dependency_id_seq'::regclass)"))
    index_id = Column(Integer, nullable=False)
    dependency_index_id = Column(ForeignKey('m2_index.id'))
    optional = Column(Boolean, nullable=False, index=True, server_default=text("false"))
    scope = Column(Text, nullable=False, server_default=text("'compile'::text"))
    group_id = Column(Text)
    artifact_id = Column(Text)
    version = Column(Text)

    dependency_index = relationship('M2Index')


class M2Index(Base):
    __tablename__ = 'm2_index'
    __table_args__ = (
        Index('m2_index_group_id_artifact_id_index', 'group_id', 'artifact_id'),
    )

    id = Column(BigInteger, unique=True, server_default=text("nextval('m2_index_id_seq_new'::regclass)"))
    group_id = Column(Text, primary_key=True, nullable=False, index=True)
    artifact_id = Column(Text, primary_key=True, nullable=False)
    version = Column(Text, primary_key=True, nullable=False)


t_m2_index2 = Table(
    'm2_index2', metadata,
    Column('no', BigInteger),
    Column('id', BigInteger)
)


class M2IndexBak(Base):
    __tablename__ = 'm2_index_bak'
    __table_args__ = (
        Index('m2_index_artifact_id_group_id_version_uindex', 'artifact_id', 'group_id', 'version', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('m2_index_id_seq'::regclass)"))
    group_id = Column(Text, nullable=False)
    artifact_id = Column(Text, nullable=False)
    version = Column(Text, nullable=False)


class M2Package(Base):
    __tablename__ = 'm2_package'

    id = Column(Integer, primary_key=True, server_default=text("nextval('m2_package_id_seq'::regclass)"))
    index_id = Column(ForeignKey('m2_index.id'), nullable=False, unique=True)
    name = Column(Text)
    description = Column(Text)
    home_page = Column(Text)
    license = Column(Text)
    organization = Column(Text)
    date = Column(Date)
    success = Column(Boolean, nullable=False, server_default=text("false"))

    index = relationship('M2Index')
