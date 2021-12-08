"""empty message

Revision ID: a69ff5e01c70
Revises: 
Create Date: 2021-12-08 11:09:43.218334

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a69ff5e01c70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('outfit',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('products', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('comments', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collection',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('outfitid', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['outfitid'], ['outfit.id'], ),
    sa.PrimaryKeyConstraint('name', 'outfitid')
    )
    op.create_table('designer',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('outfitid', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['outfitid'], ['outfit.id'], ),
    sa.PrimaryKeyConstraint('name', 'outfitid')
    )
    op.create_table('part',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('outfitid', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['outfitid'], ['outfit.id'], ),
    sa.PrimaryKeyConstraint('name', 'outfitid')
    )
    op.create_table('theme',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('outfitid', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['outfitid'], ['outfit.id'], ),
    sa.PrimaryKeyConstraint('name', 'outfitid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('theme')
    op.drop_table('part')
    op.drop_table('designer')
    op.drop_table('collection')
    op.drop_table('outfit')
    # ### end Alembic commands ###
