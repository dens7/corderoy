"""empty message

Revision ID: fdf3488b6527
Revises: 
Create Date: 2021-12-13 14:47:58.604544

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fdf3488b6527'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('outfits',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.UnicodeText(), nullable=True),
    sa.Column('desc', sa.UnicodeText(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('themes', postgresql.ARRAY(sa.UnicodeText()), nullable=True),
    sa.Column('designers', postgresql.ARRAY(sa.UnicodeText()), nullable=True),
    sa.Column('collections', postgresql.ARRAY(sa.UnicodeText()), nullable=True),
    sa.Column('parts', postgresql.ARRAY(sa.UnicodeText()), nullable=True),
    sa.Column('products', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('comments', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('outfits')
    # ### end Alembic commands ###
