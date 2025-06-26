import sys
import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from alembic import context

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.config.database import Base
from app.models import *

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = create_engine(config.get_main_option("sqlalchemy.url"))
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()